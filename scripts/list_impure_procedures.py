#!/usr/bin/env python3
"""List Fortran procedures that are not declared pure.

The audit distinguishes procedure implementations from declarations inside
interface blocks.  It also reports conservative, mechanically detectable
reasons why an implementation may need review before PURE can be added.
Only Git-tracked free-form Fortran sources are scanned by default.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote, urlparse


PROCEDURE_RE = re.compile(
    r"^\s*(?P<prefix>.*?)\b(?P<kind>subroutine|function)\s+"
    r"(?P<name>[a-z][a-z0-9_]*)\b",
    re.IGNORECASE,
)
END_PROCEDURE_RE = re.compile(r"^\s*end\s+(subroutine|function)\b", re.IGNORECASE)
INTERFACE_RE = re.compile(r"^\s*(?:abstract\s+)?interface\b", re.IGNORECASE)
END_INTERFACE_RE = re.compile(r"^\s*end\s+interface\b", re.IGNORECASE)
CALL_RE = re.compile(r"\bcall\s+([a-z][a-z0-9_]*)\b", re.IGNORECASE)
IO_RE = re.compile(
    r"^\s*(?:print\b|read\s*\(|write\s*\(|open\b|close\b|rewind\b|"
    r"backspace\b|flush\b|inquire\b)",
    re.IGNORECASE,
)
SAVE_RE = re.compile(r"^\s*save\b|^[^!]*\bsave\b[^!]*::", re.IGNORECASE)
DATA_RE = re.compile(r"^\s*data\b", re.IGNORECASE)
STOP_RE = re.compile(r"^\s*(?:error\s+)?stop\b", re.IGNORECASE)
IMPURE_INTRINSIC_RE = re.compile(
    r"\b(random_number|random_seed|date_and_time|cpu_time|system_clock|"
    r"execute_command_line|get_command|get_command_argument|"
    r"get_environment_variable)\s*\(",
    re.IGNORECASE,
)


@dataclass
class Procedure:
    """One procedure declaration or implementation."""

    name: str
    kind: str
    relative_path: str
    line: int
    pure: bool
    elemental: bool
    impure: bool
    interface: bool
    body: list[tuple[int, str]] = field(default_factory=list)

    @property
    def semantically_pure(self) -> bool:
        """Return whether the declaration has pure semantics."""

        return self.pure or (self.elemental and not self.impure)


@dataclass(frozen=True)
class Repository:
    """Git and publication metadata for the scanned repository."""

    root: Path
    label: str
    web_url: str | None
    commit: str | None
    sources_clean: bool | None


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Report tracked Fortran procedures not declared PURE."
    )
    parser.add_argument(
        "repository", nargs="?", type=Path, default=Path.cwd(), help="repository root"
    )
    parser.add_argument(
        "-o", "--output", type=Path, help="write Markdown here instead of stdout"
    )
    parser.add_argument(
        "--path",
        action="append",
        dest="paths",
        help="relative path to scan; repeat as needed (default: src)",
    )
    parser.add_argument(
        "--include-untracked",
        action="store_true",
        help="include untracked .f90/.F90 files",
    )
    parser.add_argument("--repository-url", help="override the detected public URL")
    return parser.parse_args()


def git_output(root: Path, *arguments: str) -> str | None:
    """Return stripped Git output, or None if Git fails."""

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
    """Convert a common GitHub remote spelling to an HTTPS page URL."""

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
    """Collect exact-revision metadata for report links."""

    is_git = git_output(root, "rev-parse", "--is-inside-work-tree") == "true"
    commit = git_output(root, "rev-parse", "HEAD") if is_git else None
    remote = url_override or (git_output(root, "remote", "get-url", "origin") if is_git else None)
    web_url = public_repository_url(remote)
    label = web_url.removeprefix("https://github.com/") if web_url else root.name
    status = None
    if is_git:
        status = git_output(
            root, "status", "--porcelain", "--untracked-files=no", "--", "*.f90", "*.F90"
        )
    return Repository(root, label, web_url, commit, status == "" if status is not None else None)


def strip_comment(line: str) -> str:
    """Remove a trailing Fortran comment while preserving quoted exclamation marks."""

    output: list[str] = []
    delimiter: str | None = None
    index = 0
    while index < len(line):
        character = line[index]
        if delimiter:
            output.append(character)
            if character == delimiter:
                if index + 1 < len(line) and line[index + 1] == delimiter:
                    output.append(line[index + 1])
                    index += 1
                else:
                    delimiter = None
        elif character in {"'", '"'}:
            delimiter = character
            output.append(character)
        elif character == "!":
            break
        else:
            output.append(character)
        index += 1
    return "".join(output)


def logical_statements(path: Path) -> list[tuple[int, str]]:
    """Join free-form continuation lines and retain starting line numbers."""

    statements: list[tuple[int, str]] = []
    fragments: list[str] = []
    start_line = 0
    for number, physical in enumerate(
        path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1
    ):
        code = strip_comment(physical).strip()
        if not code or code.startswith("#"):
            continue
        if not fragments:
            start_line = number
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


def selected_files(root: Path, paths: list[str], include_untracked: bool) -> list[Path]:
    """Return selected tracked Fortran files."""

    selected_roots = [(root / item).resolve() for item in paths]
    if not include_untracked and (root / ".git").exists():
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"], check=True, capture_output=True
        )
        names = result.stdout.decode("utf-8", errors="surrogateescape").split("\0")
        candidates = [root / name for name in names if name and Path(name).suffix.lower() == ".f90"]
    else:
        candidates = [
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix.lower() == ".f90" and "build" not in path.parts
        ]
    return sorted(
        path
        for path in candidates
        if any(path.resolve() == base or base in path.resolve().parents for base in selected_roots)
    )


def scan_file(path: Path, root: Path) -> list[Procedure]:
    """Parse procedure declarations and implementations in one source file."""

    procedures: list[Procedure] = []
    active: list[Procedure] = []
    interface_depth = 0
    relative_path = path.relative_to(root).as_posix()

    for line, statement in logical_statements(path):
        if END_PROCEDURE_RE.match(statement):
            if active:
                active.pop()
            continue
        if END_INTERFACE_RE.match(statement):
            interface_depth = max(0, interface_depth - 1)
            continue
        if INTERFACE_RE.match(statement):
            interface_depth += 1
            continue

        match = PROCEDURE_RE.match(statement)
        if match and not re.search(r"\b(?:end|procedure)\b", match.group("prefix"), re.IGNORECASE):
            prefix = match.group("prefix")
            procedure = Procedure(
                name=match.group("name").lower(),
                kind=match.group("kind").lower(),
                relative_path=relative_path,
                line=line,
                pure=bool(re.search(r"\bpure\b", prefix, re.IGNORECASE)),
                elemental=bool(re.search(r"\belemental\b", prefix, re.IGNORECASE)),
                impure=bool(re.search(r"\bimpure\b", prefix, re.IGNORECASE)),
                interface=interface_depth > 0,
            )
            procedures.append(procedure)
            active.append(procedure)
            continue

        if active:
            active[-1].body.append((line, statement))
    return procedures


def detectable_reasons(procedure: Procedure, nonpure_names: set[str]) -> list[str]:
    """Return conservative, directly detectable purity-review reasons."""

    reasons: list[str] = []
    if procedure.impure:
        reasons.append("explicitly declared `impure`")
    for line, statement in procedure.body:
        if IO_RE.match(statement):
            reasons.append(f"I/O at line {line}")
        if SAVE_RE.search(statement):
            reasons.append(f"`save` state at line {line}")
        if DATA_RE.match(statement):
            reasons.append(f"`data` initialization at line {line}")
        if STOP_RE.match(statement):
            reasons.append(f"stop statement at line {line}")
        intrinsic = IMPURE_INTRINSIC_RE.search(statement)
        if intrinsic:
            reasons.append(f"impure intrinsic `{intrinsic.group(1).lower()}` at line {line}")
        for called in CALL_RE.findall(statement):
            called = called.lower()
            if called in nonpure_names and called != procedure.name:
                reasons.append(f"calls non-pure `{called}` at line {line}")
    return list(dict.fromkeys(reasons))


def source_reference(procedure: Procedure, repository: Repository) -> str:
    """Return a commit-pinned source reference where possible."""

    label = f"{procedure.relative_path}:{procedure.line}"
    if repository.web_url and repository.commit:
        path = quote(procedure.relative_path, safe="/")
        url = f"{repository.web_url}/blob/{repository.commit}/{path}#L{procedure.line}"
        return f"[`{label}`]({url})"
    return f"`{label}`"


def markdown_report(repository: Repository, procedures: list[Procedure], paths: list[str]) -> str:
    """Create a publication-ready Markdown audit report."""

    implementations = [item for item in procedures if not item.interface]
    interfaces = [item for item in procedures if item.interface]
    remaining = [item for item in implementations if not item.semantically_pure]
    remaining_interfaces = [item for item in interfaces if not item.semantically_pure]
    nonpure_names = {item.name for item in remaining}
    classified = [(item, detectable_reasons(item, nonpure_names)) for item in remaining]
    with_reasons = [(item, reasons) for item, reasons in classified if reasons]
    review = [(item, reasons) for item, reasons in classified if not reasons]
    with_reasons.sort(key=lambda pair: (pair[0].relative_path.lower(), pair[0].line))
    review.sort(key=lambda pair: (pair[0].relative_path.lower(), pair[0].line))
    remaining_interfaces.sort(key=lambda item: (item.relative_path.lower(), item.line))

    short_commit = repository.commit[:12] if repository.commit else "working tree"
    revision = f"`{repository.label}@{short_commit}`"
    if repository.web_url and repository.commit:
        revision = f"[`{repository.label}@{short_commit}`]({repository.web_url}/commit/{repository.commit})"

    lines = [
        "# Remaining non-pure procedures",
        "",
        "This mechanically generated audit lists procedures that are not declared `pure` or implicitly pure through `elemental`.",
        "It is an inventory, not a claim that every listed procedure can safely be made pure.",
        "",
        f"- Repository revision: {revision}",
        f"- Scanned paths: {', '.join(f'`{item}`' for item in paths)}",
        f"- Implementations scanned: {len(implementations)}",
        f"- Pure implementations: {sum(item.semantically_pure for item in implementations)}",
        f"- Remaining non-pure implementations: {len(remaining)}",
        f"- Remaining non-pure interface declarations: {len(remaining_interfaces)}",
        "",
        "The reason detector is deliberately conservative. It recognizes direct I/O, saved state, `data` initialization, stop statements, selected impure intrinsics, and explicit calls to other non-pure implementations. Function references and procedure-pointer dispatch may require manual call-graph review.",
    ]
    if repository.sources_clean is False:
        lines.extend(
            [
                "",
                "**Warning:** tracked Fortran sources have uncommitted changes. Links point to the committed revision and may not exactly match this scan.",
            ]
        )

    lines.extend(
        [
            "",
            "## Procedures with mechanically detected review reasons",
            "",
            "| Procedure | Kind | Source | Detected reason(s) |",
            "|---|---|---|---|",
        ]
    )
    for procedure, reasons in with_reasons:
        lines.append(
            f"| `{procedure.name}` | {procedure.kind} | {source_reference(procedure, repository)} | "
            + "; ".join(reasons)
            + " |"
        )
    if not with_reasons:
        lines.append("| _None_ | | | |")

    lines.extend(
        [
            "",
            "## Procedures requiring semantic review",
            "",
            "No blocker recognized by this script was found. These are the best starting points for a compiler-backed purity audit, but they are not automatically proven pure.",
            "",
            "| Procedure | Kind | Source |",
            "|---|---|---|",
        ]
    )
    for procedure, _ in review:
        lines.append(
            f"| `{procedure.name}` | {procedure.kind} | {source_reference(procedure, repository)} |"
        )
    if not review:
        lines.append("| _None_ | | |")

    lines.extend(
        [
            "",
            "## Non-pure interface declarations",
            "",
            "These declarations are kept separate because they may describe external implementations rather than code defined in this repository.",
            "",
            "| Procedure | Kind | Source |",
            "|---|---|---|",
        ]
    )
    for procedure in remaining_interfaces:
        lines.append(
            f"| `{procedure.name}` | {procedure.kind} | {source_reference(procedure, repository)} |"
        )
    if not remaining_interfaces:
        lines.append("| _None_ | | |")

    counts = Counter(item.relative_path for item in remaining)
    lines.extend(
        [
            "",
            "## Remaining implementations by file",
            "",
            "| Source file | Count |",
            "|---|---:|",
        ]
    )
    for path, count in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0].lower())):
        lines.append(f"| `{path}` | {count} |")
    if not counts:
        lines.append("| _None_ | 0 |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    """Run the audit."""

    arguments = parse_arguments()
    root = arguments.repository.resolve()
    if not root.is_dir():
        print(f"ERROR: repository not found: {root}", file=sys.stderr)
        return 2
    paths = arguments.paths or ["src"]
    missing = [item for item in paths if not (root / item).exists()]
    if missing:
        print(f"ERROR: path not found: {missing[0]}", file=sys.stderr)
        return 2

    repository = repository_metadata(root, arguments.repository_url)
    procedures: list[Procedure] = []
    for path in selected_files(root, paths, arguments.include_untracked):
        procedures.extend(scan_file(path, root))
    report = markdown_report(repository, procedures, paths)
    if arguments.output:
        output = arguments.output.resolve()
        output.write_text(report, encoding="utf-8", newline="\n")
        print(f"Wrote {output}")
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
