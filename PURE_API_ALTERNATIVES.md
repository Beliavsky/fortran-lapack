# Pure alternatives to impure functions

This audit records the pure APIs available in place of the 390 function implementations that cannot themselves be declared `pure`. Each of those functions has an `intent(out)` or `intent(inout)` dummy argument, which is prohibited for a pure Fortran function.

The audit reflects the current fork, including the `determinant_into` API introduced in commit `82a21b77`. Procedure counts include all six supported real and complex kinds.

## High-level APIs

All 342 affected high-level function implementations have a pure alternative. Existing functions remain available for source compatibility.

| Impure function API or family | Implementations | Pure alternative | Form |
|---|---:|---|---|
| `det` | 6 | `determinant_into` | Subroutine |
| `eigvals`, `eigvalsh` | 24 | `eig`, `eigh` | Subroutine |
| Error-reporting `eye` and `diag` overloads | 18 | Corresponding overload without `err` | Function |
| `inv` | 6 | `invert`; also `.inv.` | Subroutine and operator |
| `lstsq`, `constrained_lstsq`, `weighted_lstsq` | 24 | `solve_lstsq`, `solve_constrained_lstsq`, `solve_weighted_lstsq` | Subroutine |
| Error-reporting `is_triangular` and `is_hessenberg` overloads | 12 | Corresponding overload without `err` | Function |
| Error-reporting `norm` and `mnorm` overloads | 228 | `get_norm` and corresponding no-error `norm` overloads | Subroutine and function |
| `pinv` | 6 | `pseudoinvert`; also `.pinv.` | Subroutine and operator |
| Allocating `solve` functions | 12 | `solve_lu` | Subroutine |
| `svdvals` | 6 | `svd` | Subroutine |
| **Total** | **342** | | |

The pure subroutine forms return numerical results through `intent(out)` or `intent(inout)` arguments. Where supported, an optional `type(la_state)` argument reports errors without making the procedure impure.

## Low-level compatibility functions

The remaining 48 implementations are specialized LAPACK compatibility helpers. They return a scalar function result while also modifying workspace or status arguments.

| Source family | Implementations | Purpose |
|---|---:|---|
| `xLANSF`, `xLANHF` | 6 | Norms of rectangular full packed matrices |
| `xLA_*RCOND*`, `xLA_*RPVGRW` in `la_lapack_others_sm` | 24 | Reciprocal-condition and pivot-growth helpers |
| `xLA_PORCOND`, `xLA_PORPVGRW` | 9 | Positive-definite condition and pivot-growth helpers |
| `xLA_GBRCOND`, `xLA_GERCOND` | 6 | General and banded condition helpers |
| `xLA_HERPVGRW` | 3 | Hermitian-indefinite pivot-growth helpers |
| **Total** | **48** | |

These low-level functions currently have no parallel subroutine API. Adding 48 public wrappers would increase the API surface without helping existing internal code: no pure implementation in this repository calls them. A subroutine companion should therefore be added only when a downstream pure caller needs a particular family. The numerical body should then be shared between the compatibility function and its pure subroutine rather than copied.

## Compatibility policy

- Do not remove or rename existing function interfaces.
- Prefer an existing pure API in new code.
- Put numerical work in one pure implementation and keep the impure function as a thin wrapper.
- Add low-level subroutine companions by family and only in response to a demonstrated use case.
