#!/usr/bin/env python3
"""Compare pure Fortran procedure declarations in two source trees.

The report distinguishes procedures that have a same-named, non-pure
declaration in the comparison tree from procedures that are not found there.
Only Git-tracked .f90/.F90 files are scanned when a tree is a Git repository.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urlparse


PROCEDURE_RE = re.compile(
    r"\b(subroutine|function)\s+([a-z][a-z0-9_]*)\b", re.IGNORECASE
)
END_PROCEDURE_RE = re.compile(r"^\s*end\s+(subroutine|function)\b", re.IGNORECASE)
PURE_RE = re.compile(r"\bpure\b", re.IGNORECASE)
IMPURE_RE = re.compile(r"\bimpure\b", re.IGNORECASE)
ELEMENTAL_RE = re.compile(r"\belemental\b", re.IGNORECASE)


@dataclass(frozen=True)
class Declaration:
    """Location and purity attributes of one procedure declaration."""

    name: str
    relative_path: str
    line: int
    explicit_pure: bool
    elemental: bool
    impure: bool

    @property
    def semantically_pure(self) -> bool:
        """Return whether Fortran considers this declaration pure."""

        return self.explicit_pure or (self.elemental and not self.impure)

    @property
    def attributes(self) -> str:
        """Return the relevant declaration attributes for the report."""

        values: list[str] = []
        if self.impure:
            values.append("impure")
        if self.explicit_pure:
            values.append("pure")
        if self.elemental:
            values.append("elemental")
        return " ".join(values) if values else "none"


@dataclass(frozen=True)
class Repository:
    """Publication metadata for one source tree."""

    root: Path
    label: str
    web_url: str | None
    commit: str | None
    fortran_sources_clean: bool | None


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "List procedures explicitly declared PURE in one Fortran tree but "
            "without a pure declaration in another tree."
        )
    )
    parser.add_argument("mine", type=Path, help="Your repository or source tree")
    parser.add_argument("other", type=Path, help="Comparison repository or source tree")
    parser.add_argument(
        "-o", "--output", type=Path, help="Write Markdown to this file instead of stdout"
    )
    parser.add_argument(
        "--include-untracked",
        action="store_true",
        help="Scan all source files rather than only Git-tracked files",
    )
    parser.add_argument(
        "--mine-url",
        help="Public repository URL for the first tree; otherwise detect origin",
    )
    parser.add_argument(
        "--other-url",
        help="Public repository URL for the second tree; otherwise detect origin",
    )
    return parser.parse_args()


def git_output(root: Path, *arguments: str) -> str | None:
    """Return stripped Git output, or None when the command is unavailable."""

    try:
        result = subprocess.run(
            ["git", "-C", str(root), *arguments],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def public_repository_url(remote: str | None) -> str | None:
    """Convert a common GitHub remote form to a public HTTPS URL."""

    if not remote:
        return None
    value = remote.strip().rstrip("/")
    if value.startswith("git@github.com:"):
        value = "https://github.com/" + value.removeprefix("git@github.com:")
    elif value.startswith("ssh://git@github.com/"):
        value = "https://github.com/" + value.removeprefix("ssh://git@github.com/")
    if value.endswith(".git"):
        value = value[:-4]
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"} and parsed.netloc.lower() == "github.com":
        return "https://github.com" + parsed.path
    return None


def repository_metadata(root: Path, url_override: str | None) -> Repository:
    """Collect revision and publication metadata for a source tree."""

    is_git_repository = git_output(root, "rev-parse", "--is-inside-work-tree") == "true"
    commit = git_output(root, "rev-parse", "HEAD") if is_git_repository else None
    remote = url_override or (
        git_output(root, "remote", "get-url", "origin") if is_git_repository else None
    )
    web_url = public_repository_url(remote)
    if web_url:
        label = web_url.removeprefix("https://github.com/")
    else:
        label = root.name

    clean: bool | None = None
    if is_git_repository:
        status = git_output(
            root,
            "status",
            "--porcelain",
            "--untracked-files=no",
            "--",
            "*.f90",
            "*.F90",
        )
        clean = status == ""

    return Repository(
        root=root,
        label=label,
        web_url=web_url,
        commit=commit,
        fortran_sources_clean=clean,
    )


def tracked_fortran_files(root: Path, include_untracked: bool) -> list[Path]:
    """Return relevant Fortran files under *root*."""

    if not include_untracked and (root / ".git").exists():
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
        relative_names = result.stdout.decode("utf-8", errors="surrogateescape").split("\0")
        return [
            root / name
            for name in relative_names
            if name and Path(name).suffix.lower() == ".f90"
        ]

    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() == ".f90"
        and ".git" not in path.parts
        and "build" not in path.parts
    )


def strip_fortran_comment(line: str) -> str:
    """Remove a Fortran comment while preserving exclamation marks in strings."""

    result: list[str] = []
    quote: str | None = None
    index = 0
    while index < len(line):
        character = line[index]
        if quote is not None:
            result.append(character)
            if character == quote:
                if index + 1 < len(line) and line[index + 1] == quote:
                    result.append(line[index + 1])
                    index += 1
                else:
                    quote = None
        elif character in {"'", '"'}:
            quote = character
            result.append(character)
        elif character == "!":
            break
        else:
            result.append(character)
        index += 1
    return "".join(result)


def logical_statements(path: Path) -> list[tuple[int, str]]:
    """Join free-form continuation lines and retain each starting line number."""

    statements: list[tuple[int, str]] = []
    fragments: list[str] = []
    start_line = 0

    for line_number, physical_line in enumerate(
        path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1
    ):
        code = strip_fortran_comment(physical_line).strip()
        if not code or code.startswith("#"):
            continue

        if not fragments:
            start_line = line_number
        elif code.startswith("&"):
            code = code[1:].lstrip()

        continued = code.endswith("&")
        if continued:
            code = code[:-1].rstrip()
        fragments.append(code)

        if not continued:
            statements.append((start_line, " ".join(fragments)))
            fragments = []

    if fragments:
        statements.append((start_line, " ".join(fragments)))
    return statements


def scan_tree(root: Path, include_untracked: bool) -> dict[str, list[Declaration]]:
    """Collect procedure declarations indexed by lowercase procedure name."""

    declarations: dict[str, list[Declaration]] = defaultdict(list)
    for path in tracked_fortran_files(root, include_untracked):
        relative_path = path.relative_to(root).as_posix()
        for line_number, statement in logical_statements(path):
            if END_PROCEDURE_RE.match(statement):
                continue
            match = PROCEDURE_RE.search(statement)
            if match is None:
                continue

            prefix = statement[: match.start()]
            if re.search(r"\b(module\s+)?procedure\b", prefix, re.IGNORECASE):
                continue

            name = match.group(2).lower()
            declarations[name].append(
                Declaration(
                    name=name,
                    relative_path=relative_path,
                    line=line_number,
                    explicit_pure=bool(PURE_RE.search(prefix)),
                    elemental=bool(ELEMENTAL_RE.search(prefix)),
                    impure=bool(IMPURE_RE.search(prefix)),
                )
            )
    return declarations


def reference(declaration: Declaration, repository: Repository) -> str:
    """Format a verifiable source reference."""

    label = f"{declaration.relative_path}:{declaration.line}"
    if repository.web_url and repository.commit:
        encoded_path = quote(declaration.relative_path, safe="/")
        url = (
            f"{repository.web_url}/blob/{repository.commit}/"
            f"{encoded_path}#L{declaration.line}"
        )
        return f"[`{label}`]({url})"
    return f"`{label}`"


def joined_references(
    declarations: list[Declaration],
    repository: Repository,
    show_attributes: bool,
) -> str:
    """Format one or more declaration references."""

    items: list[str] = []
    for declaration in declarations:
        item = reference(declaration, repository)
        if show_attributes:
            item += f" ({declaration.attributes})"
        items.append(item)
    return "<br>".join(items)


def markdown_report(
    mine_repository: Repository,
    other_repository: Repository,
    mine: dict[str, list[Declaration]],
    other: dict[str, list[Declaration]],
) -> str:
    """Build the Markdown comparison report."""

    candidates: list[tuple[str, list[Declaration], list[Declaration]]] = []
    missing: list[tuple[str, list[Declaration]]] = []

    for name, mine_declarations in mine.items():
        mine_explicit = [item for item in mine_declarations if item.explicit_pure]
        if not mine_explicit:
            continue
        other_declarations = other.get(name, [])
        if any(item.semantically_pure for item in other_declarations):
            continue
        if other_declarations:
            candidates.append((name, mine_explicit, other_declarations))
        else:
            missing.append((name, mine_explicit))

    candidates.sort(key=lambda item: item[0])
    missing.sort(key=lambda item: item[0])

    def revision(repository: Repository) -> str:
        """Format a repository and exact revision for Markdown."""

        short_commit = repository.commit[:12] if repository.commit else "working tree"
        text = f"{repository.label}@{short_commit}"
        if repository.web_url and repository.commit:
            return f"[`{text}`]({repository.web_url}/commit/{repository.commit})"
        return f"`{text}`"

    lines = [
        "# Pure procedure differences",
        "",
        "This report compares exact revisions of two `fortran-lapack` source trees.",
        "It was generated by `scripts/compare_pure_procedures.py`.",
        "",
        f"- Mine: {revision(mine_repository)}",
        f"- Other: {revision(other_repository)}",
        "- An `elemental` procedure without `impure` is treated as implicitly pure.",
        f"- Same-named procedures lacking purity in the other tree: {len(candidates)}",
        f"- Pure procedure names not found in the other tree: {len(missing)}",
    ]
    dirty_repositories = [
        repository.label
        for repository in (mine_repository, other_repository)
        if repository.fortran_sources_clean is False
    ]
    if dirty_repositories:
        lines.extend(
            [
                "",
                "**Warning:** Tracked Fortran sources have uncommitted changes in "
                + ", ".join(f"`{name}`" for name in dirty_repositories)
                + ". The links point to committed revisions and may not exactly match the scan.",
            ]
        )
    lines.extend(
        [
            "",
            "## Same-named procedures not pure in the other tree",
            "",
            "These are direct declaration comparisons by procedure name.",
            "",
            "| Procedure | Mine | Other |",
            "|---|---|---|",
        ]
    )
    lines.extend(
        f"| `{name}` | {joined_references(mine_items, mine_repository, False)} | "
        f"{joined_references(other_items, other_repository, True)} |"
        for name, mine_items, other_items in candidates
    )
    if not candidates:
        lines.append("| _None_ | | |")

    lines.extend(
        [
            "",
            "## Pure procedure names not found in the other tree",
            "",
            "These may have been renamed or removed, so they are not direct purity differences.",
            "",
            "| Procedure | Mine |",
            "|---|---|",
        ]
    )
    lines.extend(
        f"| `{name}` | {joined_references(mine_items, mine_repository, False)} |"
        for name, mine_items in missing
    )
    if not missing:
        lines.append("| _None_ | |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    """Run the comparison."""

    arguments = parse_arguments()
    mine_root = arguments.mine.resolve()
    other_root = arguments.other.resolve()
    for root in (mine_root, other_root):
        if not root.is_dir():
            print(f"ERROR: directory not found: {root}", file=sys.stderr)
            return 2

    mine_repository = repository_metadata(mine_root, arguments.mine_url)
    other_repository = repository_metadata(other_root, arguments.other_url)
    mine = scan_tree(mine_root, arguments.include_untracked)
    other = scan_tree(other_root, arguments.include_untracked)
    report = markdown_report(mine_repository, other_repository, mine, other)

    if arguments.output is None:
        sys.stdout.write(report)
    else:
        output = arguments.output.resolve()
        output.write_text(report, encoding="utf-8", newline="\n")
        print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
