# Pure callable alternatives

| Impure function | Pure callable alternative |
|---|---|
| `det` | `determinant_into` or `.det.` |
| `eigvals`, `eigvalsh` | `eig`, `eigh` |
| `inv` | `invert` or `.inv.` |
| `lstsq` | `solve_lstsq` |
| `constrained_lstsq` | `solve_constrained_lstsq` |
| `weighted_lstsq` | `solve_weighted_lstsq` |
| Error-reporting `norm` | `get_norm` |
| `pinv` | `pseudoinvert` or `.pinv.` |
| Allocating `solve` | `solve_lu` |
| `svdvals` | `svd` |
