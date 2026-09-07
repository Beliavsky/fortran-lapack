# Remaining non-pure procedures

This mechanically generated audit lists procedures that are not declared `pure` or implicitly pure through `elemental`.
It is an inventory, not a claim that every listed procedure can safely be made pure.

- Repository revision: [`Beliavsky/fortran-lapack@b94871396611`](https://github.com/Beliavsky/fortran-lapack/commit/b948713966113d648c1c01d52c347c5f548c0f2e)
- Scanned paths: `src`
- Implementations scanned: 4071
- Pure implementations: 3227
- Remaining non-pure implementations: 844
- Remaining non-pure interface declarations: 290

The reason detector is deliberately conservative. It recognizes direct I/O, saved state, `data` initialization, stop statements, selected impure intrinsics, and explicit calls to other non-pure implementations. Function references and procedure-pointer dispatch may require manual call-graph review.

## Procedures with mechanically detected review reasons

| Procedure | Kind | Source | Detected reason(s) |
|---|---|---|---|
| `la_eigvals_standard_s` | function | [`src/la_eigs.f90:400`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L400) | calls non-pure `la_eig_standard_s` at line 424 |
| `la_eigvals_noerr_standard_s` | function | [`src/la_eigs.f90:428`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L428) | calls non-pure `la_eig_standard_s` at line 450 |
| `la_eigvals_generalized_s` | function | [`src/la_eigs.f90:600`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L600) | calls non-pure `la_eig_generalized_s` at line 627 |
| `la_eigvals_noerr_generalized_s` | function | [`src/la_eigs.f90:631`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L631) | calls non-pure `la_eig_generalized_s` at line 656 |
| `la_eigvalsh_s` | function | [`src/la_eigs.f90:841`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L841) | calls non-pure `la_eigh_s` at line 865 |
| `la_eigvalsh_noerr_s` | function | [`src/la_eigs.f90:870`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L870) | calls non-pure `la_eigh_s` at line 892 |
| `la_eigvals_standard_d` | function | [`src/la_eigs.f90:1010`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1010) | calls non-pure `la_eig_standard_d` at line 1034 |
| `la_eigvals_noerr_standard_d` | function | [`src/la_eigs.f90:1038`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1038) | calls non-pure `la_eig_standard_d` at line 1060 |
| `la_eigvals_generalized_d` | function | [`src/la_eigs.f90:1210`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1210) | calls non-pure `la_eig_generalized_d` at line 1237 |
| `la_eigvals_noerr_generalized_d` | function | [`src/la_eigs.f90:1241`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1241) | calls non-pure `la_eig_generalized_d` at line 1266 |
| `la_eigvalsh_d` | function | [`src/la_eigs.f90:1451`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1451) | calls non-pure `la_eigh_d` at line 1475 |
| `la_eigvalsh_noerr_d` | function | [`src/la_eigs.f90:1480`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1480) | calls non-pure `la_eigh_d` at line 1502 |
| `la_eigvals_standard_q` | function | [`src/la_eigs.f90:1620`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1620) | calls non-pure `la_eig_standard_q` at line 1644 |
| `la_eigvals_noerr_standard_q` | function | [`src/la_eigs.f90:1648`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1648) | calls non-pure `la_eig_standard_q` at line 1670 |
| `la_eigvals_generalized_q` | function | [`src/la_eigs.f90:1820`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1820) | calls non-pure `la_eig_generalized_q` at line 1847 |
| `la_eigvals_noerr_generalized_q` | function | [`src/la_eigs.f90:1851`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1851) | calls non-pure `la_eig_generalized_q` at line 1876 |
| `la_eigvalsh_q` | function | [`src/la_eigs.f90:2061`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2061) | calls non-pure `la_eigh_q` at line 2085 |
| `la_eigvalsh_noerr_q` | function | [`src/la_eigs.f90:2090`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2090) | calls non-pure `la_eigh_q` at line 2112 |
| `la_eigvals_standard_c` | function | [`src/la_eigs.f90:2230`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2230) | calls non-pure `la_eig_standard_c` at line 2254 |
| `la_eigvals_noerr_standard_c` | function | [`src/la_eigs.f90:2258`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2258) | calls non-pure `la_eig_standard_c` at line 2280 |
| `la_eigvals_generalized_c` | function | [`src/la_eigs.f90:2419`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2419) | calls non-pure `la_eig_generalized_c` at line 2446 |
| `la_eigvals_noerr_generalized_c` | function | [`src/la_eigs.f90:2450`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2450) | calls non-pure `la_eig_generalized_c` at line 2475 |
| `la_eigvalsh_c` | function | [`src/la_eigs.f90:2649`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2649) | calls non-pure `la_eigh_c` at line 2673 |
| `la_eigvalsh_noerr_c` | function | [`src/la_eigs.f90:2678`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2678) | calls non-pure `la_eigh_c` at line 2700 |
| `la_eigvals_standard_z` | function | [`src/la_eigs.f90:2819`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2819) | calls non-pure `la_eig_standard_z` at line 2843 |
| `la_eigvals_noerr_standard_z` | function | [`src/la_eigs.f90:2847`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2847) | calls non-pure `la_eig_standard_z` at line 2869 |
| `la_eigvals_generalized_z` | function | [`src/la_eigs.f90:3008`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3008) | calls non-pure `la_eig_generalized_z` at line 3035 |
| `la_eigvals_noerr_generalized_z` | function | [`src/la_eigs.f90:3039`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3039) | calls non-pure `la_eig_generalized_z` at line 3064 |
| `la_eigvalsh_z` | function | [`src/la_eigs.f90:3238`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3238) | calls non-pure `la_eigh_z` at line 3262 |
| `la_eigvalsh_noerr_z` | function | [`src/la_eigs.f90:3267`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3267) | calls non-pure `la_eigh_z` at line 3289 |
| `la_eigvals_standard_w` | function | [`src/la_eigs.f90:3408`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3408) | calls non-pure `la_eig_standard_w` at line 3432 |
| `la_eigvals_noerr_standard_w` | function | [`src/la_eigs.f90:3436`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3436) | calls non-pure `la_eig_standard_w` at line 3458 |
| `la_eigvals_generalized_w` | function | [`src/la_eigs.f90:3597`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3597) | calls non-pure `la_eig_generalized_w` at line 3624 |
| `la_eigvals_noerr_generalized_w` | function | [`src/la_eigs.f90:3628`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3628) | calls non-pure `la_eig_generalized_w` at line 3653 |
| `la_eigvalsh_w` | function | [`src/la_eigs.f90:3827`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3827) | calls non-pure `la_eigh_w` at line 3851 |
| `la_eigvalsh_noerr_w` | function | [`src/la_eigs.f90:3856`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3856) | calls non-pure `la_eigh_w` at line 3878 |
| `la_real_eig_standard_s` | subroutine | [`src/la_eigs.f90:4030`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4030) | calls non-pure `la_eig_standard_s` at line 4057 |
| `la_real_eig_generalized_s` | subroutine | [`src/la_eigs.f90:4073`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4073) | calls non-pure `la_eig_generalized_s` at line 4104 |
| `la_real_eig_standard_d` | subroutine | [`src/la_eigs.f90:4153`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4153) | calls non-pure `la_eig_standard_d` at line 4180 |
| `la_real_eig_generalized_d` | subroutine | [`src/la_eigs.f90:4196`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4196) | calls non-pure `la_eig_generalized_d` at line 4227 |
| `la_real_eig_standard_q` | subroutine | [`src/la_eigs.f90:4276`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4276) | calls non-pure `la_eig_standard_q` at line 4303 |
| `la_real_eig_generalized_q` | subroutine | [`src/la_eigs.f90:4319`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L4319) | calls non-pure `la_eig_generalized_q` at line 4350 |
| `la_sgges` | subroutine | [`src/la_lapack_eigv_gen.f90:113`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L113) | calls non-pure `la_shgeqz` at line 289 |
| `la_dgges` | subroutine | [`src/la_lapack_eigv_gen.f90:432`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L432) | calls non-pure `la_dhgeqz` at line 608 |
| `la_qgges` | subroutine | [`src/la_lapack_eigv_gen.f90:751`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L751) | calls non-pure `la_qhgeqz` at line 927 |
| `la_sggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:1073`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L1073) | calls non-pure `la_shgeqz` at line 1280 |
| `la_dggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:1443`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L1443) | calls non-pure `la_dhgeqz` at line 1650 |
| `la_qggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:1813`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L1813) | calls non-pure `la_qhgeqz` at line 2020 |
| `la_sggev` | subroutine | [`src/la_lapack_eigv_gen.f90:2171`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L2171) | calls non-pure `la_shgeqz` at line 2349 |
| `la_dggev` | subroutine | [`src/la_lapack_eigv_gen.f90:2469`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L2469) | calls non-pure `la_dhgeqz` at line 2647 |
| `la_qggev` | subroutine | [`src/la_lapack_eigv_gen.f90:2767`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L2767) | calls non-pure `la_qhgeqz` at line 2945 |
| `la_sggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:3071`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L3071) | calls non-pure `la_shgeqz` at line 3290 |
| `la_dggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:3465`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L3465) | calls non-pure `la_dhgeqz` at line 3685 |
| `la_qggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:3860`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L3860) | calls non-pure `la_qhgeqz` at line 4080 |
| `la_sgees` | subroutine | [`src/la_lapack_eigv_gen.f90:4249`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L4249) | calls non-pure `la_shseqr` at line 4310; calls non-pure `la_shseqr` at line 4377; calls non-pure `la_strsen` at line 4391 |
| `la_qgees` | subroutine | [`src/la_lapack_eigv_gen.f90:4741`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L4741) | calls non-pure `la_qhseqr` at line 4802; calls non-pure `la_qhseqr` at line 4869; calls non-pure `la_qtrsen` at line 4883 |
| `la_sgeesx` | subroutine | [`src/la_lapack_eigv_gen.f90:4994`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L4994) | calls non-pure `la_shseqr` at line 5069; calls non-pure `la_shseqr` at line 5142; calls non-pure `la_strsen` at line 5160 |
| `la_qgeesx` | subroutine | [`src/la_lapack_eigv_gen.f90:5582`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L5582) | calls non-pure `la_qhseqr` at line 5657; calls non-pure `la_qhseqr` at line 5730; calls non-pure `la_qtrsen` at line 5748 |
| `la_sgeev` | subroutine | [`src/la_lapack_eigv_gen.f90:5868`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L5868) | calls non-pure `la_shseqr` at line 5932; calls non-pure `la_shseqr` at line 5945; calls non-pure `la_shseqr` at line 5956; calls non-pure `la_shseqr` at line 6016; calls non-pure `la_shseqr` at line 6036; calls non-pure `la_shseqr` at line 6042 |
| `la_qgeev` | subroutine | [`src/la_lapack_eigv_gen.f90:6386`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L6386) | calls non-pure `la_qhseqr` at line 6450; calls non-pure `la_qhseqr` at line 6463; calls non-pure `la_qhseqr` at line 6474; calls non-pure `la_qhseqr` at line 6534; calls non-pure `la_qhseqr` at line 6554; calls non-pure `la_qhseqr` at line 6560 |
| `la_sgeevx` | subroutine | [`src/la_lapack_eigv_gen.f90:6661`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L6661) | calls non-pure `la_shseqr` at line 6739; calls non-pure `la_shseqr` at line 6746; calls non-pure `la_shseqr` at line 6750; calls non-pure `la_shseqr` at line 6753; calls non-pure `la_shseqr` at line 6834; calls non-pure `la_shseqr` at line 6854; calls non-pure `la_shseqr` at line 6866; calls non-pure `la_strsna` at line 6880 |
| `la_qgeevx` | subroutine | [`src/la_lapack_eigv_gen.f90:7285`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L7285) | calls non-pure `la_qhseqr` at line 7363; calls non-pure `la_qhseqr` at line 7370; calls non-pure `la_qhseqr` at line 7374; calls non-pure `la_qhseqr` at line 7377; calls non-pure `la_qhseqr` at line 7458; calls non-pure `la_qhseqr` at line 7478; calls non-pure `la_qhseqr` at line 7490; calls non-pure `la_qtrsna` at line 7504 |
| `la_sgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:7599`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L7599) | calls non-pure `la_slaqz0` at line 7688; calls non-pure `la_slaqz0` at line 7772 |
| `la_dgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:7913`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L7913) | calls non-pure `la_dlaqz0` at line 8002; calls non-pure `la_dlaqz0` at line 8086 |
| `la_qgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:8227`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L8227) | calls non-pure `la_qlaqz0` at line 8316; calls non-pure `la_qlaqz0` at line 8400 |
| `la_sggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:8531`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L8531) | calls non-pure `la_slaqz0` at line 8612; calls non-pure `la_slaqz0` at line 8616; calls non-pure `la_slaqz0` at line 8708 |
| `la_dggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:8826`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L8826) | calls non-pure `la_dlaqz0` at line 8909; calls non-pure `la_dlaqz0` at line 8916; calls non-pure `la_dlaqz0` at line 9008 |
| `la_qggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:9126`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L9126) | calls non-pure `la_qlaqz0` at line 9209; calls non-pure `la_qlaqz0` at line 9216; calls non-pure `la_qlaqz0` at line 9308 |
| `la_cgges` | subroutine | [`src/la_lapack_eigv_gen.f90:9432`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L9432) | calls non-pure `la_chgeqz` at line 9603 |
| `la_zgges` | subroutine | [`src/la_lapack_eigv_gen.f90:9683`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L9683) | calls non-pure `la_zhgeqz` at line 9854 |
| `la_wgges` | subroutine | [`src/la_lapack_eigv_gen.f90:9934`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L9934) | calls non-pure `la_whgeqz` at line 10105 |
| `la_cggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:10188`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L10188) | calls non-pure `la_chgeqz` at line 10396 |
| `la_zggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:10497`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L10497) | calls non-pure `la_zhgeqz` at line 10705 |
| `la_wggesx` | subroutine | [`src/la_lapack_eigv_gen.f90:10806`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L10806) | calls non-pure `la_whgeqz` at line 11014 |
| `la_cggev` | subroutine | [`src/la_lapack_eigv_gen.f90:11109`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L11109) | calls non-pure `la_chgeqz` at line 11291 |
| `la_zggev` | subroutine | [`src/la_lapack_eigv_gen.f90:11378`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L11378) | calls non-pure `la_zhgeqz` at line 11560 |
| `la_wggev` | subroutine | [`src/la_lapack_eigv_gen.f90:11647`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L11647) | calls non-pure `la_whgeqz` at line 11829 |
| `la_cggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:11922`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L11922) | calls non-pure `la_chgeqz` at line 12144 |
| `la_zggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:12269`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L12269) | calls non-pure `la_zhgeqz` at line 12491 |
| `la_wggevx` | subroutine | [`src/la_lapack_eigv_gen.f90:12616`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L12616) | calls non-pure `la_whgeqz` at line 12838 |
| `la_cgees` | subroutine | [`src/la_lapack_eigv_gen.f90:12952`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L12952) | calls non-pure `la_ctrsen` at line 13097 |
| `la_wgees` | subroutine | [`src/la_lapack_eigv_gen.f90:13294`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L13294) | calls non-pure `la_wtrsen` at line 13439 |
| `la_cgeesx` | subroutine | [`src/la_lapack_eigv_gen.f90:13472`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L13472) | calls non-pure `la_ctrsen` at line 13632 |
| `la_wgeesx` | subroutine | [`src/la_lapack_eigv_gen.f90:13876`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L13876) | calls non-pure `la_wtrsen` at line 14036 |
| `la_cgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:15740`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L15740) | calls non-pure `la_claqz0` at line 15828; calls non-pure `la_claqz0` at line 15912 |
| `la_zgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:15990`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L15990) | calls non-pure `la_zlaqz0` at line 16078; calls non-pure `la_zlaqz0` at line 16162 |
| `la_wgges3` | subroutine | [`src/la_lapack_eigv_gen.f90:16240`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L16240) | calls non-pure `la_wlaqz0` at line 16328; calls non-pure `la_wlaqz0` at line 16412 |
| `la_cggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:16486`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L16486) | calls non-pure `la_claqz0` at line 16574; calls non-pure `la_claqz0` at line 16581; calls non-pure `la_claqz0` at line 16673 |
| `la_zggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:16757`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L16757) | calls non-pure `la_zlaqz0` at line 16845; calls non-pure `la_zlaqz0` at line 16852; calls non-pure `la_zlaqz0` at line 16944 |
| `la_wggev3` | subroutine | [`src/la_lapack_eigv_gen.f90:17028`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L17028) | calls non-pure `la_wlaqz0` at line 17116; calls non-pure `la_wlaqz0` at line 17123; calls non-pure `la_wlaqz0` at line 17215 |
| `la_strsen` | subroutine | [`src/la_lapack_eigv_gen2.f90:8058`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L8058) | calls non-pure `la_strexc` at line 8177; calls non-pure `la_strsyl` at line 8194; calls non-pure `la_strsyl` at line 8214; calls non-pure `la_strsyl` at line 8218 |
| `la_qtrsen` | subroutine | [`src/la_lapack_eigv_gen2.f90:8448`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L8448) | calls non-pure `la_qtrexc` at line 8567; calls non-pure `la_qtrsyl` at line 8584; calls non-pure `la_qtrsyl` at line 8604; calls non-pure `la_qtrsyl` at line 8608 |
| `la_strsna` | subroutine | [`src/la_lapack_eigv_gen2.f90:8641`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L8641) | calls non-pure `la_strexc` at line 8789; calls non-pure `la_slaqtr` at line 8847; calls non-pure `la_slaqtr` at line 8852; calls non-pure `la_slaqtr` at line 8858; calls non-pure `la_slaqtr` at line 8863 |
| `la_qtrsna` | subroutine | [`src/la_lapack_eigv_gen2.f90:9131`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L9131) | calls non-pure `la_qtrexc` at line 9279; calls non-pure `la_qlaqtr` at line 9337; calls non-pure `la_qlaqtr` at line 9342; calls non-pure `la_qlaqtr` at line 9348; calls non-pure `la_qlaqtr` at line 9353 |
| `la_shseqr` | subroutine | [`src/la_lapack_eigv_gen2.f90:9377`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L9377) | calls non-pure `la_slaqr0` at line 9446; calls non-pure `la_slaqr0` at line 9476; calls non-pure `la_slaqr0` at line 9489; calls non-pure `la_slaqr0` at line 9499 |
| `la_qhseqr` | subroutine | [`src/la_lapack_eigv_gen2.f90:9669`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L9669) | calls non-pure `la_qlaqr0` at line 9738; calls non-pure `la_qlaqr0` at line 9768; calls non-pure `la_qlaqr0` at line 9781; calls non-pure `la_qlaqr0` at line 9791 |
| `la_ctrsen` | subroutine | [`src/la_lapack_eigv_gen2.f90:13376`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L13376) | calls non-pure `la_ctrsyl` at line 13466; calls non-pure `la_ctrsyl` at line 13486; calls non-pure `la_ctrsyl` at line 13490 |
| `la_wtrsen` | subroutine | [`src/la_lapack_eigv_gen2.f90:13650`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L13650) | calls non-pure `la_wtrsyl` at line 13740; calls non-pure `la_wtrsyl` at line 13760; calls non-pure `la_wtrsyl` at line 13764 |
| `la_slaqr2` | subroutine | [`src/la_lapack_eigv_gen3.f90:5046`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L5046) | calls non-pure `la_strexc` at line 5165; calls non-pure `la_strexc` at line 5182; calls non-pure `la_strexc` at line 5231 |
| `la_qlaqr2` | subroutine | [`src/la_lapack_eigv_gen3.f90:5652`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L5652) | calls non-pure `la_qtrexc` at line 5771; calls non-pure `la_qtrexc` at line 5788; calls non-pure `la_qtrexc` at line 5837 |
| `la_slaqr0` | subroutine | [`src/la_lapack_eigv_gen3.f90:5953`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L5953) | calls non-pure `la_slaqr3` at line 6044; calls non-pure `la_slaqr3` at line 6142; calls non-pure `la_slaqr4` at line 6196 |
| `la_qlaqr0` | subroutine | [`src/la_lapack_eigv_gen3.f90:6691`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L6691) | calls non-pure `la_qlaqr3` at line 6782; calls non-pure `la_qlaqr3` at line 6880; calls non-pure `la_qlaqr4` at line 6934 |
| `la_slaqr3` | subroutine | [`src/la_lapack_eigv_gen3.f90:7062`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L7062) | calls non-pure `la_slaqr4` at line 7100; calls non-pure `la_slaqr4` at line 7157; calls non-pure `la_strexc` at line 7191; calls non-pure `la_strexc` at line 7208; calls non-pure `la_strexc` at line 7257 |
| `la_qlaqr3` | subroutine | [`src/la_lapack_eigv_gen3.f90:7684`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L7684) | calls non-pure `la_qlaqr4` at line 7722; calls non-pure `la_qlaqr4` at line 7779; calls non-pure `la_qtrexc` at line 7813; calls non-pure `la_qtrexc` at line 7830; calls non-pure `la_qtrexc` at line 7879 |
| `la_slaqr4` | subroutine | [`src/la_lapack_eigv_gen3.f90:8001`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L8001) | calls non-pure `la_slaqr2` at line 8092; calls non-pure `la_slaqr2` at line 8190 |
| `la_qlaqr4` | subroutine | [`src/la_lapack_eigv_gen3.f90:8741`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L8741) | calls non-pure `la_qlaqr2` at line 8832; calls non-pure `la_qlaqr2` at line 8930 |
| `la_slaqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:9146`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L9146) | calls non-pure `la_shgeqz` at line 9246; calls non-pure `la_slaqz3` at line 9253; calls non-pure `la_slaqz3` at line 9423; calls non-pure `la_shgeqz` at line 9485 |
| `la_dlaqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:9538`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L9538) | calls non-pure `la_dhgeqz` at line 9638; calls non-pure `la_dlaqz3` at line 9645; calls non-pure `la_dlaqz3` at line 9815; calls non-pure `la_dhgeqz` at line 9877 |
| `la_qlaqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:9930`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L9930) | calls non-pure `la_qhgeqz` at line 10030; calls non-pure `la_qlaqz3` at line 10037; calls non-pure `la_qlaqz3` at line 10207; calls non-pure `la_qhgeqz` at line 10269 |
| `la_slaqz3` | subroutine | [`src/la_lapack_eigv_gen3.f90:10276`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L10276) | calls non-pure `la_slaqz0` at line 10309; calls non-pure `la_slaqz0` at line 10352 |
| `la_dlaqz3` | subroutine | [`src/la_lapack_eigv_gen3.f90:10548`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L10548) | calls non-pure `la_dlaqz0` at line 10581; calls non-pure `la_dlaqz0` at line 10624 |
| `la_qlaqz3` | subroutine | [`src/la_lapack_eigv_gen3.f90:10820`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L10820) | calls non-pure `la_qlaqz0` at line 10853; calls non-pure `la_qlaqz0` at line 10896 |
| `la_claqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:17618`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L17618) | calls non-pure `la_chgeqz` at line 17720; calls non-pure `la_claqz2` at line 17727; calls non-pure `la_claqz2` at line 17886; calls non-pure `la_chgeqz` at line 17925 |
| `la_zlaqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:17970`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L17970) | calls non-pure `la_zhgeqz` at line 18072; calls non-pure `la_zlaqz2` at line 18079; calls non-pure `la_zlaqz2` at line 18238; calls non-pure `la_zhgeqz` at line 18277 |
| `la_wlaqz0` | subroutine | [`src/la_lapack_eigv_gen3.f90:18322`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L18322) | calls non-pure `la_whgeqz` at line 18424; calls non-pure `la_wlaqz2` at line 18431; calls non-pure `la_wlaqz2` at line 18590; calls non-pure `la_whgeqz` at line 18629 |
| `la_claqz2` | subroutine | [`src/la_lapack_eigv_gen3.f90:18636`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L18636) | calls non-pure `la_claqz0` at line 18667; calls non-pure `la_claqz0` at line 18709 |
| `la_zlaqz2` | subroutine | [`src/la_lapack_eigv_gen3.f90:18824`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L18824) | calls non-pure `la_zlaqz0` at line 18855; calls non-pure `la_zlaqz0` at line 18897 |
| `la_wlaqz2` | subroutine | [`src/la_lapack_eigv_gen3.f90:19012`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L19012) | calls non-pure `la_wlaqz0` at line 19043; calls non-pure `la_wlaqz0` at line 19085 |
| `la_strexc` | subroutine | [`src/la_lapack_eigv_gen_aux.f90:2823`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen_aux.f90#L2823) | calls non-pure `la_slaexc` at line 2898; calls non-pure `la_slaexc` at line 2916; calls non-pure `la_slaexc` at line 2924; calls non-pure `la_slaexc` at line 2932; calls non-pure `la_slaexc` at line 2941; calls non-pure `la_slaexc` at line 2943; calls non-pure `la_slaexc` at line 2960; calls non-pure `la_slaexc` at line 2978; calls non-pure `la_slaexc` at line 2986; calls non-pure `la_slaexc` at line 2994; calls non-pure `la_slaexc` at line 3003; calls non-pure `la_slaexc` at line 3005 |
| `la_qtrexc` | subroutine | [`src/la_lapack_eigv_gen_aux.f90:3231`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen_aux.f90#L3231) | calls non-pure `la_qlaexc` at line 3306; calls non-pure `la_qlaexc` at line 3324; calls non-pure `la_qlaexc` at line 3332; calls non-pure `la_qlaexc` at line 3340; calls non-pure `la_qlaexc` at line 3349; calls non-pure `la_qlaexc` at line 3351; calls non-pure `la_qlaexc` at line 3368; calls non-pure `la_qlaexc` at line 3386; calls non-pure `la_qlaexc` at line 3394; calls non-pure `la_qlaexc` at line 3402; calls non-pure `la_qlaexc` at line 3411; calls non-pure `la_qlaexc` at line 3413 |
| `la_sgesvdq` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:6827`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L6827) | calls non-pure `la_sgesvd` at line 6959; calls non-pure `la_sgesvd` at line 6978; calls non-pure `la_sgesvd` at line 6981; calls non-pure `la_sgesvd` at line 7001; calls non-pure `la_sgesvd` at line 7004; calls non-pure `la_sgesvd` at line 7049; calls non-pure `la_sgesvd` at line 7058; calls non-pure `la_sgesvd` at line 7071; calls non-pure `la_sgesvd` at line 7080; calls non-pure `la_sgesvd` at line 7297; calls non-pure `la_sgesvd` at line 7302; calls non-pure `la_sgesvd` at line 7322; calls non-pure `la_sgesvd` at line 7339; calls non-pure `la_sgesvd` at line 7376; calls non-pure `la_sgesvd` at line 7400; calls non-pure `la_sgesvd` at line 7420; calls non-pure `la_sgesvd` at line 7431; calls non-pure `la_sgesvd` at line 7455; calls non-pure `la_sgesvd` at line 7506; calls non-pure `la_sgesvd` at line 7550; calls non-pure `la_sgesvd` at line 7578; calls non-pure `la_sgesvd` at line 7608; calls non-pure `la_sgesvd` at line 7631 |
| `la_qgesvdq` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:8558`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L8558) | calls non-pure `la_qgesvd` at line 8689; calls non-pure `la_qgesvd` at line 8708; calls non-pure `la_qgesvd` at line 8711; calls non-pure `la_qgesvd` at line 8731; calls non-pure `la_qgesvd` at line 8734; calls non-pure `la_qgesvd` at line 8779; calls non-pure `la_qgesvd` at line 8788; calls non-pure `la_qgesvd` at line 8801; calls non-pure `la_qgesvd` at line 8810; calls non-pure `la_qgesvd` at line 9027; calls non-pure `la_qgesvd` at line 9032; calls non-pure `la_qgesvd` at line 9052; calls non-pure `la_qgesvd` at line 9069; calls non-pure `la_qgesvd` at line 9106; calls non-pure `la_qgesvd` at line 9130; calls non-pure `la_qgesvd` at line 9150; calls non-pure `la_qgesvd` at line 9161; calls non-pure `la_qgesvd` at line 9185; calls non-pure `la_qgesvd` at line 9236; calls non-pure `la_qgesvd` at line 9280; calls non-pure `la_qgesvd` at line 9308; calls non-pure `la_qgesvd` at line 9338; calls non-pure `la_qgesvd` at line 9361 |
| `la_cgesvdq` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:16761`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L16761) | calls non-pure `la_cgesvd` at line 16889; calls non-pure `la_cgesvd` at line 16908; calls non-pure `la_cgesvd` at line 16911; calls non-pure `la_cgesvd` at line 16931; calls non-pure `la_cgesvd` at line 16934; calls non-pure `la_cgesvd` at line 16979; calls non-pure `la_cgesvd` at line 16988; calls non-pure `la_cgesvd` at line 17001; calls non-pure `la_cgesvd` at line 17010; calls non-pure `la_cgesvd` at line 17227; calls non-pure `la_cgesvd` at line 17233; calls non-pure `la_cgesvd` at line 17254; calls non-pure `la_cgesvd` at line 17272; calls non-pure `la_cgesvd` at line 17310; calls non-pure `la_cgesvd` at line 17335; calls non-pure `la_cgesvd` at line 17356; calls non-pure `la_cgesvd` at line 17367; calls non-pure `la_cgesvd` at line 17393; calls non-pure `la_cgesvd` at line 17447; calls non-pure `la_cgesvd` at line 17493; calls non-pure `la_cgesvd` at line 17521; calls non-pure `la_cgesvd` at line 17552; calls non-pure `la_cgesvd` at line 17576 |
| `la_wgesvdq` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:18516`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L18516) | calls non-pure `la_wgesvd` at line 18643; calls non-pure `la_wgesvd` at line 18662; calls non-pure `la_wgesvd` at line 18665; calls non-pure `la_wgesvd` at line 18685; calls non-pure `la_wgesvd` at line 18688; calls non-pure `la_wgesvd` at line 18733; calls non-pure `la_wgesvd` at line 18742; calls non-pure `la_wgesvd` at line 18755; calls non-pure `la_wgesvd` at line 18764; calls non-pure `la_wgesvd` at line 18981; calls non-pure `la_wgesvd` at line 18987; calls non-pure `la_wgesvd` at line 19008; calls non-pure `la_wgesvd` at line 19026; calls non-pure `la_wgesvd` at line 19064; calls non-pure `la_wgesvd` at line 19089; calls non-pure `la_wgesvd` at line 19110; calls non-pure `la_wgesvd` at line 19121; calls non-pure `la_wgesvd` at line 19147; calls non-pure `la_wgesvd` at line 19201; calls non-pure `la_wgesvd` at line 19247; calls non-pure `la_wgesvd` at line 19275; calls non-pure `la_wgesvd` at line 19306; calls non-pure `la_wgesvd` at line 19330 |
| `la_sspgv` | subroutine | [`src/la_lapack_eigv_sym.F90:5407`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5407) | calls non-pure `la_sspev` at line 5453 |
| `la_dspgv` | subroutine | [`src/la_lapack_eigv_sym.F90:5490`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5490) | calls non-pure `la_dspev` at line 5536 |
| `la_qspgv` | subroutine | [`src/la_lapack_eigv_sym.F90:5573`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5573) | calls non-pure `la_qspev` at line 5619 |
| `la_sspgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:5659`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5659) | calls non-pure `la_sspevx` at line 5731 |
| `la_dspgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:5770`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5770) | calls non-pure `la_dspevx` at line 5842 |
| `la_qspgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:5881`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5881) | calls non-pure `la_qspevx` at line 5953 |
| `la_ssygv` | subroutine | [`src/la_lapack_eigv_sym.F90:7055`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L7055) | calls non-pure `la_ssyev` at line 7119 |
| `la_qsygv` | subroutine | [`src/la_lapack_eigv_sym.F90:7255`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L7255) | calls non-pure `la_qsyev` at line 7319 |
| `la_ssygvx` | subroutine | [`src/la_lapack_eigv_sym.F90:7357`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L7357) | calls non-pure `la_ssyevx` at line 7447 |
| `la_qsygvx` | subroutine | [`src/la_lapack_eigv_sym.F90:7613`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L7613) | calls non-pure `la_qsyevx` at line 7703 |
| `la_ssygvd` | subroutine | [`src/la_lapack_eigv_sym.F90:8676`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L8676) | calls non-pure `la_ssyevd` at line 8754 |
| `la_qsygvd` | subroutine | [`src/la_lapack_eigv_sym.F90:8918`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L8918) | calls non-pure `la_qsyevd` at line 8996 |
| `la_sspgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:10166`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L10166) | calls non-pure `la_sspevd` at line 10240 |
| `la_dspgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:10289`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L10289) | calls non-pure `la_dspevd` at line 10363 |
| `la_qspgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:10412`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L10412) | calls non-pure `la_qspevd` at line 10486 |
| `la_chegv` | subroutine | [`src/la_lapack_eigv_sym.F90:16751`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16751) | calls non-pure `la_cheev` at line 16816 |
| `la_zhegv` | subroutine | [`src/la_lapack_eigv_sym.F90:16852`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16852) | calls non-pure `la_zheev` at line 16917 |
| `la_whegv` | subroutine | [`src/la_lapack_eigv_sym.F90:16953`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16953) | calls non-pure `la_wheev` at line 17018 |
| `la_chegvx` | subroutine | [`src/la_lapack_eigv_sym.F90:17056`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17056) | calls non-pure `la_cheevx` at line 17146 |
| `la_zhegvx` | subroutine | [`src/la_lapack_eigv_sym.F90:17184`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17184) | calls non-pure `la_zheevx` at line 17274 |
| `la_whegvx` | subroutine | [`src/la_lapack_eigv_sym.F90:17312`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17312) | calls non-pure `la_wheevx` at line 17402 |
| `la_chpgv` | subroutine | [`src/la_lapack_eigv_sym.F90:18381`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18381) | calls non-pure `la_chpev` at line 18428 |
| `la_zhpgv` | subroutine | [`src/la_lapack_eigv_sym.F90:18465`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18465) | calls non-pure `la_zhpev` at line 18512 |
| `la_whpgv` | subroutine | [`src/la_lapack_eigv_sym.F90:18549`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18549) | calls non-pure `la_whpev` at line 18596 |
| `la_chpgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:18636`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18636) | calls non-pure `la_chpevx` at line 18708 |
| `la_zhpgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:18747`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18747) | calls non-pure `la_zhpevx` at line 18819 |
| `la_whpgvx` | subroutine | [`src/la_lapack_eigv_sym.F90:18858`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18858) | calls non-pure `la_whpevx` at line 18930 |
| `la_chegvd` | subroutine | [`src/la_lapack_eigv_sym.F90:22068`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22068) | calls non-pure `la_cheevd` at line 22154 |
| `la_zhegvd` | subroutine | [`src/la_lapack_eigv_sym.F90:22200`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22200) | calls non-pure `la_zheevd` at line 22286 |
| `la_whegvd` | subroutine | [`src/la_lapack_eigv_sym.F90:22332`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22332) | calls non-pure `la_wheevd` at line 22418 |
| `la_chpgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:22890`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22890) | calls non-pure `la_chpevd` at line 22971 |
| `la_zhpgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:23022`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L23022) | calls non-pure `la_zhpevd` at line 23103 |
| `la_whpgvd` | subroutine | [`src/la_lapack_eigv_sym.F90:23154`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L23154) | calls non-pure `la_whpevd` at line 23235 |
| `la_slacon` | subroutine | [`src/la_lapack_solve_aux.f90:433`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L433) | `save` state at line 456 |
| `la_dlacon` | subroutine | [`src/la_lapack_solve_aux.f90:553`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L553) | `save` state at line 576 |
| `la_qlacon` | subroutine | [`src/la_lapack_solve_aux.f90:673`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L673) | `save` state at line 696 |
| `la_clacon` | subroutine | [`src/la_lapack_solve_aux.f90:1433`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L1433) | `save` state at line 1455 |
| `la_zlacon` | subroutine | [`src/la_lapack_solve_aux.f90:1558`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L1558) | `save` state at line 1580 |
| `la_wlacon` | subroutine | [`src/la_lapack_solve_aux.f90:1683`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_aux.f90#L1683) | `save` state at line 1705 |
| `la_slstsq_one` | function | [`src/la_least_squares.f90:475`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L475) | calls non-pure `la_ssolve_lstsq_one` at line 502 |
| `la_dlstsq_one` | function | [`src/la_least_squares.f90:700`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L700) | calls non-pure `la_dsolve_lstsq_one` at line 727 |
| `la_qlstsq_one` | function | [`src/la_least_squares.f90:925`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L925) | calls non-pure `la_qsolve_lstsq_one` at line 952 |
| `la_clstsq_one` | function | [`src/la_least_squares.f90:1151`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1151) | calls non-pure `la_csolve_lstsq_one` at line 1178 |
| `la_zlstsq_one` | function | [`src/la_least_squares.f90:1391`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1391) | calls non-pure `la_zsolve_lstsq_one` at line 1418 |
| `la_wlstsq_one` | function | [`src/la_least_squares.f90:1631`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1631) | calls non-pure `la_wsolve_lstsq_one` at line 1658 |
| `la_slstsq_multiple` | function | [`src/la_least_squares.f90:1870`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1870) | calls non-pure `la_ssolve_lstsq_multiple` at line 1897 |
| `la_dlstsq_multiple` | function | [`src/la_least_squares.f90:2095`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2095) | calls non-pure `la_dsolve_lstsq_multiple` at line 2122 |
| `la_qlstsq_multiple` | function | [`src/la_least_squares.f90:2320`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2320) | calls non-pure `la_qsolve_lstsq_multiple` at line 2347 |
| `la_clstsq_multiple` | function | [`src/la_least_squares.f90:2546`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2546) | calls non-pure `la_csolve_lstsq_multiple` at line 2573 |
| `la_zlstsq_multiple` | function | [`src/la_least_squares.f90:2786`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2786) | calls non-pure `la_zsolve_lstsq_multiple` at line 2813 |
| `la_wlstsq_multiple` | function | [`src/la_least_squares.f90:3026`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3026) | calls non-pure `la_wsolve_lstsq_multiple` at line 3053 |
| `la_ssolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:3342`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3342) | calls non-pure `la_sconstrained_lstsq_space` at line 3396 |
| `la_sconstrained_lstsq` | function | [`src/la_least_squares.f90:3426`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3426) | calls non-pure `la_ssolve_constrained_lstsq` at line 3444 |
| `la_sweighted_lstsq` | function | [`src/la_least_squares.f90:3449`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3449) | calls non-pure `la_ssolve_weighted_lstsq` at line 3473 |
| `la_ssolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:3478`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3478) | calls non-pure `la_ssolve_lstsq_one` at line 3546 |
| `la_dsolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:3592`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3592) | calls non-pure `la_dconstrained_lstsq_space` at line 3646 |
| `la_dconstrained_lstsq` | function | [`src/la_least_squares.f90:3676`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3676) | calls non-pure `la_dsolve_constrained_lstsq` at line 3694 |
| `la_dweighted_lstsq` | function | [`src/la_least_squares.f90:3699`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3699) | calls non-pure `la_dsolve_weighted_lstsq` at line 3723 |
| `la_dsolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:3728`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3728) | calls non-pure `la_dsolve_lstsq_one` at line 3796 |
| `la_qsolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:3842`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3842) | calls non-pure `la_qconstrained_lstsq_space` at line 3896 |
| `la_qconstrained_lstsq` | function | [`src/la_least_squares.f90:3926`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3926) | calls non-pure `la_qsolve_constrained_lstsq` at line 3944 |
| `la_qweighted_lstsq` | function | [`src/la_least_squares.f90:3949`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3949) | calls non-pure `la_qsolve_weighted_lstsq` at line 3973 |
| `la_qsolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:3978`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3978) | calls non-pure `la_qsolve_lstsq_one` at line 4046 |
| `la_csolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:4092`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4092) | calls non-pure `la_cconstrained_lstsq_space` at line 4146 |
| `la_cconstrained_lstsq` | function | [`src/la_least_squares.f90:4176`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4176) | calls non-pure `la_csolve_constrained_lstsq` at line 4194 |
| `la_cweighted_lstsq` | function | [`src/la_least_squares.f90:4199`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4199) | calls non-pure `la_csolve_weighted_lstsq` at line 4223 |
| `la_csolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:4228`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4228) | calls non-pure `la_csolve_lstsq_one` at line 4296 |
| `la_zsolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:4342`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4342) | calls non-pure `la_zconstrained_lstsq_space` at line 4396 |
| `la_zconstrained_lstsq` | function | [`src/la_least_squares.f90:4426`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4426) | calls non-pure `la_zsolve_constrained_lstsq` at line 4444 |
| `la_zweighted_lstsq` | function | [`src/la_least_squares.f90:4449`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4449) | calls non-pure `la_zsolve_weighted_lstsq` at line 4473 |
| `la_zsolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:4478`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4478) | calls non-pure `la_zsolve_lstsq_one` at line 4546 |
| `la_wsolve_constrained_lstsq` | subroutine | [`src/la_least_squares.f90:4592`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4592) | calls non-pure `la_wconstrained_lstsq_space` at line 4646 |
| `la_wconstrained_lstsq` | function | [`src/la_least_squares.f90:4676`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4676) | calls non-pure `la_wsolve_constrained_lstsq` at line 4694 |
| `la_wweighted_lstsq` | function | [`src/la_least_squares.f90:4699`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4699) | calls non-pure `la_wsolve_weighted_lstsq` at line 4723 |
| `la_wsolve_weighted_lstsq` | subroutine | [`src/la_least_squares.f90:4728`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4728) | calls non-pure `la_wsolve_lstsq_one` at line 4796 |
| `la_pseudoinverse_s` | function | [`src/la_pinv.f90:237`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L237) | calls non-pure `la_pseudoinvert_s` at line 251 |
| `la_pinv_s_operator` | function | [`src/la_pinv.f90:256`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L256) | calls non-pure `la_pseudoinvert_s` at line 266 |
| `la_pseudoinverse_d` | function | [`src/la_pinv.f90:336`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L336) | calls non-pure `la_pseudoinvert_d` at line 350 |
| `la_pinv_d_operator` | function | [`src/la_pinv.f90:355`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L355) | calls non-pure `la_pseudoinvert_d` at line 365 |
| `la_pseudoinverse_q` | function | [`src/la_pinv.f90:435`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L435) | calls non-pure `la_pseudoinvert_q` at line 449 |
| `la_pinv_q_operator` | function | [`src/la_pinv.f90:454`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L454) | calls non-pure `la_pseudoinvert_q` at line 464 |
| `la_pseudoinverse_c` | function | [`src/la_pinv.f90:534`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L534) | calls non-pure `la_pseudoinvert_c` at line 548 |
| `la_pinv_c_operator` | function | [`src/la_pinv.f90:553`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L553) | calls non-pure `la_pseudoinvert_c` at line 563 |
| `la_pseudoinverse_z` | function | [`src/la_pinv.f90:633`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L633) | calls non-pure `la_pseudoinvert_z` at line 647 |
| `la_pinv_z_operator` | function | [`src/la_pinv.f90:652`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L652) | calls non-pure `la_pseudoinvert_z` at line 662 |
| `la_pseudoinverse_w` | function | [`src/la_pinv.f90:732`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L732) | calls non-pure `la_pseudoinvert_w` at line 746 |
| `la_pinv_w_operator` | function | [`src/la_pinv.f90:751`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L751) | calls non-pure `la_pseudoinvert_w` at line 761 |
| `la_s_schur` | subroutine | [`src/la_schur.f90:191`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L191) | calls non-pure `get_schur_s_workspace` at line 274 |
| `la_real_eig_s_schur` | subroutine | [`src/la_schur.f90:355`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L355) | calls non-pure `la_s_schur` at line 381 |
| `la_q_schur` | subroutine | [`src/la_schur.f90:695`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L695) | calls non-pure `get_schur_q_workspace` at line 778 |
| `la_real_eig_q_schur` | subroutine | [`src/la_schur.f90:859`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L859) | calls non-pure `la_q_schur` at line 885 |
| `la_c_schur` | subroutine | [`src/la_schur.f90:947`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L947) | calls non-pure `get_schur_c_workspace` at line 1030 |
| `la_real_eig_c_schur` | subroutine | [`src/la_schur.f90:1109`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L1109) | calls non-pure `la_c_schur` at line 1135 |
| `la_w_schur` | subroutine | [`src/la_schur.f90:1447`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L1447) | calls non-pure `get_schur_w_workspace` at line 1530 |
| `la_real_eig_w_schur` | subroutine | [`src/la_schur.f90:1609`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L1609) | calls non-pure `la_w_schur` at line 1635 |
| `la_svdvals_s` | function | [`src/la_svd.f90:113`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L113) | calls non-pure `la_svd_s` at line 136 |
| `la_svdvals_d` | function | [`src/la_svd.f90:300`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L300) | calls non-pure `la_svd_d` at line 323 |
| `la_svdvals_q` | function | [`src/la_svd.f90:487`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L487) | calls non-pure `la_svd_q` at line 510 |
| `la_svdvals_c` | function | [`src/la_svd.f90:674`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L674) | calls non-pure `la_svd_c` at line 697 |
| `la_svdvals_z` | function | [`src/la_svd.f90:867`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L867) | calls non-pure `la_svd_z` at line 890 |
| `la_svdvals_w` | function | [`src/la_svd.f90:1060`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L1060) | calls non-pure `la_svd_w` at line 1083 |

## Procedures requiring semantic review

No blocker recognized by this script was found. These are the best starting points for a compiler-backed purity audit, but they are not automatically proven pure.

| Procedure | Kind | Source |
|---|---|---|
| `la_sdeterminant` | function | [`src/la_determinant.f90:71`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L71) |
| `la_ddeterminant` | function | [`src/la_determinant.f90:239`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L239) |
| `la_qdeterminant` | function | [`src/la_determinant.f90:407`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L407) |
| `la_cdeterminant` | function | [`src/la_determinant.f90:575`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L575) |
| `la_zdeterminant` | function | [`src/la_determinant.f90:743`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L743) |
| `la_wdeterminant` | function | [`src/la_determinant.f90:911`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_determinant.f90#L911) |
| `la_eig_standard_s` | subroutine | [`src/la_eigs.f90:454`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L454) |
| `la_eig_generalized_s` | subroutine | [`src/la_eigs.f90:660`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L660) |
| `la_eigh_s` | subroutine | [`src/la_eigs.f90:898`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L898) |
| `la_eig_standard_d` | subroutine | [`src/la_eigs.f90:1064`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1064) |
| `la_eig_generalized_d` | subroutine | [`src/la_eigs.f90:1270`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1270) |
| `la_eigh_d` | subroutine | [`src/la_eigs.f90:1508`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1508) |
| `la_eig_standard_q` | subroutine | [`src/la_eigs.f90:1674`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1674) |
| `la_eig_generalized_q` | subroutine | [`src/la_eigs.f90:1880`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L1880) |
| `la_eigh_q` | subroutine | [`src/la_eigs.f90:2118`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2118) |
| `la_eig_standard_c` | subroutine | [`src/la_eigs.f90:2284`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2284) |
| `la_eig_generalized_c` | subroutine | [`src/la_eigs.f90:2479`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2479) |
| `la_eigh_c` | subroutine | [`src/la_eigs.f90:2706`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2706) |
| `la_eig_standard_z` | subroutine | [`src/la_eigs.f90:2873`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L2873) |
| `la_eig_generalized_z` | subroutine | [`src/la_eigs.f90:3068`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3068) |
| `la_eigh_z` | subroutine | [`src/la_eigs.f90:3295`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3295) |
| `la_eig_standard_w` | subroutine | [`src/la_eigs.f90:3462`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3462) |
| `la_eig_generalized_w` | subroutine | [`src/la_eigs.f90:3657`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3657) |
| `la_eigh_w` | subroutine | [`src/la_eigs.f90:3884`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eigs.f90#L3884) |
| `la_eye_s_errhandle` | function | [`src/la_eye.f90:1020`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1020) |
| `la_eye_d_errhandle` | function | [`src/la_eye.f90:1071`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1071) |
| `la_eye_q_errhandle` | function | [`src/la_eye.f90:1122`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1122) |
| `la_eye_c_errhandle` | function | [`src/la_eye.f90:1173`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1173) |
| `la_eye_z_errhandle` | function | [`src/la_eye.f90:1224`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1224) |
| `la_eye_w_errhandle` | function | [`src/la_eye.f90:1275`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1275) |
| `la_diag_s_errhandle_from_scalar` | function | [`src/la_eye.f90:1324`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1324) |
| `la_diag_s_errhandle_from_array` | function | [`src/la_eye.f90:1368`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1368) |
| `la_diag_d_errhandle_from_scalar` | function | [`src/la_eye.f90:1412`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1412) |
| `la_diag_d_errhandle_from_array` | function | [`src/la_eye.f90:1456`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1456) |
| `la_diag_q_errhandle_from_scalar` | function | [`src/la_eye.f90:1500`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1500) |
| `la_diag_q_errhandle_from_array` | function | [`src/la_eye.f90:1544`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1544) |
| `la_diag_c_errhandle_from_scalar` | function | [`src/la_eye.f90:1588`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1588) |
| `la_diag_c_errhandle_from_array` | function | [`src/la_eye.f90:1632`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1632) |
| `la_diag_z_errhandle_from_scalar` | function | [`src/la_eye.f90:1676`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1676) |
| `la_diag_z_errhandle_from_array` | function | [`src/la_eye.f90:1720`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1720) |
| `la_diag_w_errhandle_from_scalar` | function | [`src/la_eye.f90:1764`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1764) |
| `la_diag_w_errhandle_from_array` | function | [`src/la_eye.f90:1808`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_eye.f90#L1808) |
| `la_invert_split_s` | subroutine | [`src/la_inverse.f90:176`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L176) |
| `la_inverse_s` | function | [`src/la_inverse.f90:215`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L215) |
| `la_invert_split_d` | subroutine | [`src/la_inverse.f90:323`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L323) |
| `la_inverse_d` | function | [`src/la_inverse.f90:362`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L362) |
| `la_invert_split_q` | subroutine | [`src/la_inverse.f90:470`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L470) |
| `la_inverse_q` | function | [`src/la_inverse.f90:509`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L509) |
| `la_invert_split_c` | subroutine | [`src/la_inverse.f90:617`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L617) |
| `la_inverse_c` | function | [`src/la_inverse.f90:656`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L656) |
| `la_invert_split_z` | subroutine | [`src/la_inverse.f90:764`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L764) |
| `la_inverse_z` | function | [`src/la_inverse.f90:803`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L803) |
| `la_invert_split_w` | subroutine | [`src/la_inverse.f90:911`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L911) |
| `la_inverse_w` | function | [`src/la_inverse.f90:950`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_inverse.f90#L950) |
| `la_slangb` | function | [`src/la_lapack_blas_like_mnorm.f90:99`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L99) |
| `la_dlangb` | function | [`src/la_lapack_blas_like_mnorm.f90:174`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L174) |
| `la_qlangb` | function | [`src/la_lapack_blas_like_mnorm.f90:249`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L249) |
| `la_slanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:768`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L768) |
| `la_dlanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:840`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L840) |
| `la_qlanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:912`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L912) |
| `la_slansb` | function | [`src/la_lapack_blas_like_mnorm.f90:985`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L985) |
| `la_dlansb` | function | [`src/la_lapack_blas_like_mnorm.f90:1090`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L1090) |
| `la_qlansb` | function | [`src/la_lapack_blas_like_mnorm.f90:1195`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L1195) |
| `la_slansf` | function | [`src/la_lapack_blas_like_mnorm.f90:1301`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L1301) |
| `la_dlansf` | function | [`src/la_lapack_blas_like_mnorm.f90:2005`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L2005) |
| `la_qlansf` | function | [`src/la_lapack_blas_like_mnorm.f90:2709`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L2709) |
| `la_slansp` | function | [`src/la_lapack_blas_like_mnorm.f90:3414`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L3414) |
| `la_dlansp` | function | [`src/la_lapack_blas_like_mnorm.f90:3538`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L3538) |
| `la_qlansp` | function | [`src/la_lapack_blas_like_mnorm.f90:3662`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L3662) |
| `la_slantb` | function | [`src/la_lapack_blas_like_mnorm.f90:4260`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L4260) |
| `la_dlantb` | function | [`src/la_lapack_blas_like_mnorm.f90:4453`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L4453) |
| `la_qlantb` | function | [`src/la_lapack_blas_like_mnorm.f90:4646`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L4646) |
| `la_slantp` | function | [`src/la_lapack_blas_like_mnorm.f90:4840`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L4840) |
| `la_dlantp` | function | [`src/la_lapack_blas_like_mnorm.f90:5046`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L5046) |
| `la_qlantp` | function | [`src/la_lapack_blas_like_mnorm.f90:5252`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L5252) |
| `la_slantr` | function | [`src/la_lapack_blas_like_mnorm.f90:5459`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L5459) |
| `la_dlantr` | function | [`src/la_lapack_blas_like_mnorm.f90:5645`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L5645) |
| `la_qlantr` | function | [`src/la_lapack_blas_like_mnorm.f90:5831`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L5831) |
| `la_clangb` | function | [`src/la_lapack_blas_like_mnorm.f90:6018`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6018) |
| `la_zlangb` | function | [`src/la_lapack_blas_like_mnorm.f90:6093`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6093) |
| `la_wlangb` | function | [`src/la_lapack_blas_like_mnorm.f90:6168`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6168) |
| `la_clanhb` | function | [`src/la_lapack_blas_like_mnorm.f90:6687`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6687) |
| `la_zlanhb` | function | [`src/la_lapack_blas_like_mnorm.f90:6806`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6806) |
| `la_wlanhb` | function | [`src/la_lapack_blas_like_mnorm.f90:6925`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L6925) |
| `la_clanhe` | function | [`src/la_lapack_blas_like_mnorm.f90:7045`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L7045) |
| `la_zlanhe` | function | [`src/la_lapack_blas_like_mnorm.f90:7155`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L7155) |
| `la_wlanhe` | function | [`src/la_lapack_blas_like_mnorm.f90:7265`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L7265) |
| `la_clanhf` | function | [`src/la_lapack_blas_like_mnorm.f90:7376`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L7376) |
| `la_zlanhf` | function | [`src/la_lapack_blas_like_mnorm.f90:8596`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L8596) |
| `la_wlanhf` | function | [`src/la_lapack_blas_like_mnorm.f90:9816`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L9816) |
| `la_clanhp` | function | [`src/la_lapack_blas_like_mnorm.f90:11037`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11037) |
| `la_zlanhp` | function | [`src/la_lapack_blas_like_mnorm.f90:11165`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11165) |
| `la_wlanhp` | function | [`src/la_lapack_blas_like_mnorm.f90:11293`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11293) |
| `la_clanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:11422`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11422) |
| `la_zlanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:11494`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11494) |
| `la_wlanhs` | function | [`src/la_lapack_blas_like_mnorm.f90:11566`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11566) |
| `la_clansb` | function | [`src/la_lapack_blas_like_mnorm.f90:11829`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11829) |
| `la_zlansb` | function | [`src/la_lapack_blas_like_mnorm.f90:11934`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L11934) |
| `la_wlansb` | function | [`src/la_lapack_blas_like_mnorm.f90:12039`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12039) |
| `la_clansp` | function | [`src/la_lapack_blas_like_mnorm.f90:12145`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12145) |
| `la_zlansp` | function | [`src/la_lapack_blas_like_mnorm.f90:12278`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12278) |
| `la_wlansp` | function | [`src/la_lapack_blas_like_mnorm.f90:12411`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12411) |
| `la_clansy` | function | [`src/la_lapack_blas_like_mnorm.f90:12545`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12545) |
| `la_zlansy` | function | [`src/la_lapack_blas_like_mnorm.f90:12641`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12641) |
| `la_wlansy` | function | [`src/la_lapack_blas_like_mnorm.f90:12737`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12737) |
| `la_clantb` | function | [`src/la_lapack_blas_like_mnorm.f90:12834`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L12834) |
| `la_zlantb` | function | [`src/la_lapack_blas_like_mnorm.f90:13027`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L13027) |
| `la_wlantb` | function | [`src/la_lapack_blas_like_mnorm.f90:13220`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L13220) |
| `la_clantp` | function | [`src/la_lapack_blas_like_mnorm.f90:13414`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L13414) |
| `la_zlantp` | function | [`src/la_lapack_blas_like_mnorm.f90:13620`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L13620) |
| `la_wlantp` | function | [`src/la_lapack_blas_like_mnorm.f90:13826`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L13826) |
| `la_clantr` | function | [`src/la_lapack_blas_like_mnorm.f90:14033`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L14033) |
| `la_zlantr` | function | [`src/la_lapack_blas_like_mnorm.f90:14219`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L14219) |
| `la_wlantr` | function | [`src/la_lapack_blas_like_mnorm.f90:14405`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_blas_like_mnorm.f90#L14405) |
| `la_shgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:3290`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L3290) |
| `la_dhgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:4165`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L4165) |
| `la_qhgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:5040`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L5040) |
| `la_chgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:9138`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L9138) |
| `la_zhgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:9636`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L9636) |
| `la_whgeqz` | subroutine | [`src/la_lapack_eigv_comp.f90:10134`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_comp.f90#L10134) |
| `la_cgeev` | subroutine | [`src/la_lapack_eigv_gen.f90:14075`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L14075) |
| `la_wgeev` | subroutine | [`src/la_lapack_eigv_gen.f90:14573`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L14573) |
| `la_cgeevx` | subroutine | [`src/la_lapack_eigv_gen.f90:14838`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L14838) |
| `la_wgeevx` | subroutine | [`src/la_lapack_eigv_gen.f90:15442`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen.f90#L15442) |
| `la_strsyl` | subroutine | [`src/la_lapack_eigv_gen2.f90:5428`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L5428) |
| `la_qtrsyl` | subroutine | [`src/la_lapack_eigv_gen2.f90:6750`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L6750) |
| `la_shsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:7407`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L7407) |
| `la_dhsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:7622`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L7622) |
| `la_qhsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:7837`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L7837) |
| `la_ctrsyl` | subroutine | [`src/la_lapack_eigv_gen2.f90:12177`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L12177) |
| `la_wtrsyl` | subroutine | [`src/la_lapack_eigv_gen2.f90:12629`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L12629) |
| `la_chsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:12855`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L12855) |
| `la_zhsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:13028`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L13028) |
| `la_whsein` | subroutine | [`src/la_lapack_eigv_gen2.f90:13201`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen2.f90#L13201) |
| `la_slaqtr` | subroutine | [`src/la_lapack_eigv_gen3.f90:2792`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L2792) |
| `la_qlaqtr` | subroutine | [`src/la_lapack_eigv_gen3.f90:3684`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen3.f90#L3684) |
| `la_slaexc` | subroutine | [`src/la_lapack_eigv_gen_aux.f90:2232`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen_aux.f90#L2232) |
| `la_qlaexc` | subroutine | [`src/la_lapack_eigv_gen_aux.f90:2623`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_gen_aux.f90#L2623) |
| `la_sgesvd` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:50`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L50) |
| `la_qgesvd` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:4569`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L4569) |
| `la_cgesvd` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:9426`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L9426) |
| `la_wgesvd` | subroutine | [`src/la_lapack_eigv_svd_drivers.f90:14317`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers.f90#L14317) |
| `la_sgesdd` | subroutine | [`src/la_lapack_eigv_svd_drivers2.f90:6274`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers2.f90#L6274) |
| `la_qgesdd` | subroutine | [`src/la_lapack_eigv_svd_drivers2.f90:8216`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers2.f90#L8216) |
| `la_cgesdd` | subroutine | [`src/la_lapack_eigv_svd_drivers2.f90:9186`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers2.f90#L9186) |
| `la_wgesdd` | subroutine | [`src/la_lapack_eigv_svd_drivers2.f90:12174`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_svd_drivers2.f90#L12174) |
| `la_ssbev` | subroutine | [`src/la_lapack_eigv_sym.F90:2710`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L2710) |
| `la_dsbev` | subroutine | [`src/la_lapack_eigv_sym.F90:2812`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L2812) |
| `la_qsbev` | subroutine | [`src/la_lapack_eigv_sym.F90:2914`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L2914) |
| `la_ssbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:3019`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L3019) |
| `la_dsbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:3245`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L3245) |
| `la_qsbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:3471`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L3471) |
| `la_sspev` | subroutine | [`src/la_lapack_eigv_sym.F90:4484`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L4484) |
| `la_dspev` | subroutine | [`src/la_lapack_eigv_sym.F90:4577`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L4577) |
| `la_qspev` | subroutine | [`src/la_lapack_eigv_sym.F90:4670`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L4670) |
| `la_sspevx` | subroutine | [`src/la_lapack_eigv_sym.F90:4766`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L4766) |
| `la_dspevx` | subroutine | [`src/la_lapack_eigv_sym.F90:4979`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L4979) |
| `la_qspevx` | subroutine | [`src/la_lapack_eigv_sym.F90:5192`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5192) |
| `la_ssyev` | subroutine | [`src/la_lapack_eigv_sym.F90:5988`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L5988) |
| `la_qsyev` | subroutine | [`src/la_lapack_eigv_sym.F90:6202`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L6202) |
| `la_ssyevx` | subroutine | [`src/la_lapack_eigv_sym.F90:6312`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L6312) |
| `la_qsyevx` | subroutine | [`src/la_lapack_eigv_sym.F90:6806`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L6806) |
| `la_ssyevd` | subroutine | [`src/la_lapack_eigv_sym.F90:8273`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L8273) |
| `la_qsyevd` | subroutine | [`src/la_lapack_eigv_sym.F90:8541`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L8541) |
| `la_ssbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:9038`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L9038) |
| `la_dsbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:9170`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L9170) |
| `la_qsbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:9302`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L9302) |
| `la_sspevd` | subroutine | [`src/la_lapack_eigv_sym.F90:9787`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L9787) |
| `la_dspevd` | subroutine | [`src/la_lapack_eigv_sym.F90:9912`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L9912) |
| `la_qspevd` | subroutine | [`src/la_lapack_eigv_sym.F90:10037`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L10037) |
| `la_ssyevr` | subroutine | [`src/la_lapack_eigv_sym.F90:10574`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L10574) |
| `la_qsyevr` | subroutine | [`src/la_lapack_eigv_sym.F90:11225`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L11225) |
| `la_cheev` | subroutine | [`src/la_lapack_eigv_sym.F90:14660`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L14660) |
| `la_zheev` | subroutine | [`src/la_lapack_eigv_sym.F90:14770`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L14770) |
| `la_wheev` | subroutine | [`src/la_lapack_eigv_sym.F90:14880`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L14880) |
| `la_cheevr` | subroutine | [`src/la_lapack_eigv_sym.F90:15039`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L15039) |
| `la_zheevr` | subroutine | [`src/la_lapack_eigv_sym.F90:15378`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L15378) |
| `la_wheevr` | subroutine | [`src/la_lapack_eigv_sym.F90:15717`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L15717) |
| `la_cheevx` | subroutine | [`src/la_lapack_eigv_sym.F90:16011`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16011) |
| `la_zheevx` | subroutine | [`src/la_lapack_eigv_sym.F90:16257`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16257) |
| `la_wheevx` | subroutine | [`src/la_lapack_eigv_sym.F90:16503`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L16503) |
| `la_chpev` | subroutine | [`src/la_lapack_eigv_sym.F90:17437`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17437) |
| `la_zhpev` | subroutine | [`src/la_lapack_eigv_sym.F90:17534`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17534) |
| `la_whpev` | subroutine | [`src/la_lapack_eigv_sym.F90:17631`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17631) |
| `la_chpevx` | subroutine | [`src/la_lapack_eigv_sym.F90:17731`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17731) |
| `la_zhpevx` | subroutine | [`src/la_lapack_eigv_sym.F90:17947`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L17947) |
| `la_whpevx` | subroutine | [`src/la_lapack_eigv_sym.F90:18163`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18163) |
| `la_chbev` | subroutine | [`src/la_lapack_eigv_sym.F90:18965`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L18965) |
| `la_zhbev` | subroutine | [`src/la_lapack_eigv_sym.F90:19069`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19069) |
| `la_whbev` | subroutine | [`src/la_lapack_eigv_sym.F90:19173`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19173) |
| `la_chbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:19285`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19285) |
| `la_zhbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:19434`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19434) |
| `la_whbevd` | subroutine | [`src/la_lapack_eigv_sym.F90:19583`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19583) |
| `la_chbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:19728`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19728) |
| `la_zhbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:19958`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L19958) |
| `la_whbevx` | subroutine | [`src/la_lapack_eigv_sym.F90:20188`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L20188) |
| `la_cheevd` | subroutine | [`src/la_lapack_eigv_sym.F90:21609`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L21609) |
| `la_zheevd` | subroutine | [`src/la_lapack_eigv_sym.F90:21761`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L21761) |
| `la_wheevd` | subroutine | [`src/la_lapack_eigv_sym.F90:21913`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L21913) |
| `la_chpevd` | subroutine | [`src/la_lapack_eigv_sym.F90:22463`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22463) |
| `la_zhpevd` | subroutine | [`src/la_lapack_eigv_sym.F90:22604`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22604) |
| `la_whpevd` | subroutine | [`src/la_lapack_eigv_sym.F90:22745`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_eigv_sym.F90#L22745) |
| `la_sgels` | subroutine | [`src/la_lapack_lsq.f90:78`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L78) |
| `la_qgels` | subroutine | [`src/la_lapack_lsq.f90:512`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L512) |
| `la_sgelsy` | subroutine | [`src/la_lapack_lsq.f90:744`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L744) |
| `la_qgelsy` | subroutine | [`src/la_lapack_lsq.f90:1208`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L1208) |
| `la_sgetsls` | subroutine | [`src/la_lapack_lsq.f90:1427`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L1427) |
| `la_qgetsls` | subroutine | [`src/la_lapack_lsq.f90:1899`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L1899) |
| `la_sgelsd` | subroutine | [`src/la_lapack_lsq.f90:2143`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L2143) |
| `la_qgelsd` | subroutine | [`src/la_lapack_lsq.f90:2792`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L2792) |
| `la_sgelss` | subroutine | [`src/la_lapack_lsq.f90:3103`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L3103) |
| `la_qgelss` | subroutine | [`src/la_lapack_lsq.f90:3984`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L3984) |
| `la_cgels` | subroutine | [`src/la_lapack_lsq.f90:4433`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L4433) |
| `la_wgels` | subroutine | [`src/la_lapack_lsq.f90:4867`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L4867) |
| `la_cgelsd` | subroutine | [`src/la_lapack_lsq.f90:5092`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L5092) |
| `la_wgelsd` | subroutine | [`src/la_lapack_lsq.f90:5766`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L5766) |
| `la_cgelss` | subroutine | [`src/la_lapack_lsq.f90:6091`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L6091) |
| `la_wgelss` | subroutine | [`src/la_lapack_lsq.f90:7005`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L7005) |
| `la_cgelsy` | subroutine | [`src/la_lapack_lsq.f90:7483`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L7483) |
| `la_wgelsy` | subroutine | [`src/la_lapack_lsq.f90:7929`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L7929) |
| `la_cgetsls` | subroutine | [`src/la_lapack_lsq.f90:8139`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L8139) |
| `la_wgetsls` | subroutine | [`src/la_lapack_lsq.f90:8611`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_lsq.f90#L8611) |
| `la_sla_syrcond` | function | [`src/la_lapack_others_sm.f90:751`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L751) |
| `la_dla_syrcond` | function | [`src/la_lapack_others_sm.f90:918`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L918) |
| `la_qla_syrcond` | function | [`src/la_lapack_others_sm.f90:1085`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L1085) |
| `la_sla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:1250`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L1250) |
| `la_dla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:1434`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L1434) |
| `la_qla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:1618`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L1618) |
| `la_cla_gbrcond_c` | function | [`src/la_lapack_others_sm.f90:2518`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L2518) |
| `la_zla_gbrcond_c` | function | [`src/la_lapack_others_sm.f90:2666`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L2666) |
| `la_wla_gbrcond_c` | function | [`src/la_lapack_others_sm.f90:2814`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L2814) |
| `la_cla_gercond_c` | function | [`src/la_lapack_others_sm.f90:2963`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L2963) |
| `la_zla_gercond_c` | function | [`src/la_lapack_others_sm.f90:3104`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3104) |
| `la_wla_gercond_c` | function | [`src/la_lapack_others_sm.f90:3245`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3245) |
| `la_cla_hercond_c` | function | [`src/la_lapack_others_sm.f90:3387`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3387) |
| `la_zla_hercond_c` | function | [`src/la_lapack_others_sm.f90:3537`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3537) |
| `la_wla_hercond_c` | function | [`src/la_lapack_others_sm.f90:3687`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3687) |
| `la_cla_porcond_c` | function | [`src/la_lapack_others_sm.f90:3838`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3838) |
| `la_zla_porcond_c` | function | [`src/la_lapack_others_sm.f90:3988`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L3988) |
| `la_wla_porcond_c` | function | [`src/la_lapack_others_sm.f90:4138`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4138) |
| `la_cla_syrcond_c` | function | [`src/la_lapack_others_sm.f90:4289`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4289) |
| `la_zla_syrcond_c` | function | [`src/la_lapack_others_sm.f90:4440`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4440) |
| `la_wla_syrcond_c` | function | [`src/la_lapack_others_sm.f90:4591`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4591) |
| `la_cla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:4747`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4747) |
| `la_zla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:4936`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L4936) |
| `la_wla_syrpvgrw` | function | [`src/la_lapack_others_sm.f90:5125`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_others_sm.f90#L5125) |
| `la_sppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:225`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L225) |
| `la_dppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:364`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L364) |
| `la_qppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:503`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L503) |
| `la_qdposv` | subroutine | [`src/la_lapack_solve_chol.f90:1184`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L1184) |
| `la_spbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:1500`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L1500) |
| `la_dpbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:1656`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L1656) |
| `la_qpbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:1812`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L1812) |
| `la_sposvx` | subroutine | [`src/la_lapack_solve_chol.f90:2120`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L2120) |
| `la_qposvx` | subroutine | [`src/la_lapack_solve_chol.f90:2406`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L2406) |
| `la_cppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:2695`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L2695) |
| `la_zppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:2835`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L2835) |
| `la_wppsvx` | subroutine | [`src/la_lapack_solve_chol.f90:2975`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L2975) |
| `la_zcposv` | subroutine | [`src/la_lapack_solve_chol.f90:3137`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L3137) |
| `la_wzposv` | subroutine | [`src/la_lapack_solve_chol.f90:3321`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L3321) |
| `la_cpbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:3645`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L3645) |
| `la_zpbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:3802`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L3802) |
| `la_wpbsvx` | subroutine | [`src/la_lapack_solve_chol.f90:3959`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L3959) |
| `la_cposvx` | subroutine | [`src/la_lapack_solve_chol.f90:4268`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L4268) |
| `la_zposvx` | subroutine | [`src/la_lapack_solve_chol.f90:4412`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L4412) |
| `la_wposvx` | subroutine | [`src/la_lapack_solve_chol.f90:4556`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol.f90#L4556) |
| `la_sla_porcond` | function | [`src/la_lapack_solve_chol_comp.f90:3129`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L3129) |
| `la_dla_porcond` | function | [`src/la_lapack_solve_chol_comp.f90:3288`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L3288) |
| `la_qla_porcond` | function | [`src/la_lapack_solve_chol_comp.f90:3447`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L3447) |
| `la_sla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:10381`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L10381) |
| `la_dla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:10469`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L10469) |
| `la_qla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:10557`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L10557) |
| `la_cla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:11172`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L11172) |
| `la_zla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:11265`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L11265) |
| `la_wla_porpvgrw` | function | [`src/la_lapack_solve_chol_comp.f90:11358`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_chol_comp.f90#L11358) |
| `la_sspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:242`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L242) |
| `la_dspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:320`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L320) |
| `la_qspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:398`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L398) |
| `la_ssysvx` | subroutine | [`src/la_lapack_solve_ldl.f90:1173`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L1173) |
| `la_qsysvx` | subroutine | [`src/la_lapack_solve_ldl.f90:1367`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L1367) |
| `la_cspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:1830`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L1830) |
| `la_zspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:1908`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L1908) |
| `la_wspsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:1986`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L1986) |
| `la_csysvx` | subroutine | [`src/la_lapack_solve_ldl.f90:2760`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L2760) |
| `la_zsysvx` | subroutine | [`src/la_lapack_solve_ldl.f90:2857`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L2857) |
| `la_wsysvx` | subroutine | [`src/la_lapack_solve_ldl.f90:2954`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L2954) |
| `la_chesvx` | subroutine | [`src/la_lapack_solve_ldl.f90:3747`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L3747) |
| `la_zhesvx` | subroutine | [`src/la_lapack_solve_ldl.f90:3844`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L3844) |
| `la_whesvx` | subroutine | [`src/la_lapack_solve_ldl.f90:3941`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L3941) |
| `la_chpsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:4190`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L4190) |
| `la_zhpsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:4268`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L4268) |
| `la_whpsvx` | subroutine | [`src/la_lapack_solve_ldl.f90:4346`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl.f90#L4346) |
| `la_cla_herpvgrw` | function | [`src/la_lapack_solve_ldl_comp.f90:15334`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl_comp.f90#L15334) |
| `la_zla_herpvgrw` | function | [`src/la_lapack_solve_ldl_comp.f90:15523`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl_comp.f90#L15523) |
| `la_wla_herpvgrw` | function | [`src/la_lapack_solve_ldl_comp.f90:15712`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_ldl_comp.f90#L15712) |
| `la_sgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:757`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L757) |
| `la_dgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:983`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L983) |
| `la_qgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:1206`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L1206) |
| `la_qdgesv` | subroutine | [`src/la_lapack_solve_lu.f90:1896`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L1896) |
| `la_sgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:2195`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L2195) |
| `la_dgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:2399`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L2399) |
| `la_qgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:2603`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L2603) |
| `la_cgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:3239`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L3239) |
| `la_zgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:3466`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L3466) |
| `la_wgbsvx` | subroutine | [`src/la_lapack_solve_lu.f90:3693`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L3693) |
| `la_wzgesv` | subroutine | [`src/la_lapack_solve_lu.f90:4390`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L4390) |
| `la_cgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:4695`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L4695) |
| `la_zgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:4900`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L4900) |
| `la_wgesvx` | subroutine | [`src/la_lapack_solve_lu.f90:5105`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu.f90#L5105) |
| `la_sla_gbrcond` | function | [`src/la_lapack_solve_lu_comp.f90:7440`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L7440) |
| `la_dla_gbrcond` | function | [`src/la_lapack_solve_lu_comp.f90:7598`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L7598) |
| `la_qla_gbrcond` | function | [`src/la_lapack_solve_lu_comp.f90:7756`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L7756) |
| `la_sla_gercond` | function | [`src/la_lapack_solve_lu_comp.f90:7915`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L7915) |
| `la_dla_gercond` | function | [`src/la_lapack_solve_lu_comp.f90:8065`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L8065) |
| `la_qla_gercond` | function | [`src/la_lapack_solve_lu_comp.f90:8215`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_lu_comp.f90#L8215) |
| `la_stbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:7851`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L7851) |
| `la_dtbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:7955`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L7955) |
| `la_qtbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:8059`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L8059) |
| `la_stpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:8714`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L8714) |
| `la_dtpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:8813`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L8813) |
| `la_qtpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:8912`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L8912) |
| `la_strcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:9012`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L9012) |
| `la_dtrcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:9113`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L9113) |
| `la_qtrcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:9214`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L9214) |
| `la_ctbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:18285`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L18285) |
| `la_ztbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:18394`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L18394) |
| `la_wtbcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:18503`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L18503) |
| `la_ctpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19163`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19163) |
| `la_ztpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19267`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19267) |
| `la_wtpcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19371`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19371) |
| `la_ctrcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19476`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19476) |
| `la_ztrcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19582`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19582) |
| `la_wtrcon` | subroutine | [`src/la_lapack_solve_tri_comp.f90:19688`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack_solve_tri_comp.f90#L19688) |
| `la_ssolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:515`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L515) |
| `la_dsolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:740`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L740) |
| `la_qsolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:965`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L965) |
| `la_csolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:1191`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1191) |
| `la_zsolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:1431`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1431) |
| `la_wsolve_lstsq_one` | subroutine | [`src/la_least_squares.f90:1671`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1671) |
| `la_ssolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:1910`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L1910) |
| `la_dsolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:2135`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2135) |
| `la_qsolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:2360`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2360) |
| `la_csolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:2586`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2586) |
| `la_zsolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:2826`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L2826) |
| `la_wsolve_lstsq_multiple` | subroutine | [`src/la_least_squares.f90:3066`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3066) |
| `la_sconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:3310`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3310) |
| `la_dconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:3560`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3560) |
| `la_qconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:3810`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L3810) |
| `la_cconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:4060`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4060) |
| `la_zconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:4310`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4310) |
| `la_wconstrained_lstsq_space` | subroutine | [`src/la_least_squares.f90:4560`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_least_squares.f90#L4560) |
| `la_is_triangular_s_errhandle` | function | [`src/la_matrix_property_checks.f90:1401`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1401) |
| `la_is_hessenberg_s_errhandle` | function | [`src/la_matrix_property_checks.f90:1445`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1445) |
| `la_is_triangular_d_errhandle` | function | [`src/la_matrix_property_checks.f90:1489`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1489) |
| `la_is_hessenberg_d_errhandle` | function | [`src/la_matrix_property_checks.f90:1533`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1533) |
| `la_is_triangular_q_errhandle` | function | [`src/la_matrix_property_checks.f90:1577`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1577) |
| `la_is_hessenberg_q_errhandle` | function | [`src/la_matrix_property_checks.f90:1621`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1621) |
| `la_is_triangular_c_errhandle` | function | [`src/la_matrix_property_checks.f90:1665`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1665) |
| `la_is_hessenberg_c_errhandle` | function | [`src/la_matrix_property_checks.f90:1709`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1709) |
| `la_is_triangular_z_errhandle` | function | [`src/la_matrix_property_checks.f90:1753`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1753) |
| `la_is_hessenberg_z_errhandle` | function | [`src/la_matrix_property_checks.f90:1797`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1797) |
| `la_is_triangular_w_errhandle` | function | [`src/la_matrix_property_checks.f90:1841`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1841) |
| `la_is_hessenberg_w_errhandle` | function | [`src/la_matrix_property_checks.f90:1885`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_matrix_property_checks.f90#L1885) |
| `la_norm_1d_order_err_char_s` | function | [`src/la_norms.f90:738`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L738) |
| `la_norm_2d_order_err_char_s` | function | [`src/la_norms.f90:821`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L821) |
| `la_norm_3d_order_err_char_s` | function | [`src/la_norms.f90:904`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L904) |
| `la_norm_4d_order_err_char_s` | function | [`src/la_norms.f90:987`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L987) |
| `la_norm_5d_order_err_char_s` | function | [`src/la_norms.f90:1070`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1070) |
| `la_norm_6d_order_err_char_s` | function | [`src/la_norms.f90:1153`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1153) |
| `la_norm_7d_order_err_char_s` | function | [`src/la_norms.f90:1236`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1236) |
| `la_norm_2d_to_1d_err_char_s` | function | [`src/la_norms.f90:1325`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1325) |
| `la_norm_3d_to_2d_err_char_s` | function | [`src/la_norms.f90:1421`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1421) |
| `la_norm_4d_to_3d_err_char_s` | function | [`src/la_norms.f90:1518`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1518) |
| `la_norm_5d_to_4d_err_char_s` | function | [`src/la_norms.f90:1617`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1617) |
| `la_norm_6d_to_5d_err_char_s` | function | [`src/la_norms.f90:1716`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1716) |
| `la_norm_7d_to_6d_err_char_s` | function | [`src/la_norms.f90:1817`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1817) |
| `matrix_norm_char_s` | function | [`src/la_norms.f90:1906`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1906) |
| `matrix_norm_3d_to_1d_char_s` | function | [`src/la_norms.f90:1956`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L1956) |
| `matrix_norm_4d_to_2d_char_s` | function | [`src/la_norms.f90:2052`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2052) |
| `matrix_norm_5d_to_3d_char_s` | function | [`src/la_norms.f90:2149`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2149) |
| `matrix_norm_6d_to_4d_char_s` | function | [`src/la_norms.f90:2247`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2247) |
| `matrix_norm_7d_to_5d_char_s` | function | [`src/la_norms.f90:2346`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2346) |
| `la_norm_1d_order_err_int_s` | function | [`src/la_norms.f90:2463`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2463) |
| `la_norm_2d_order_err_int_s` | function | [`src/la_norms.f90:2546`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2546) |
| `la_norm_3d_order_err_int_s` | function | [`src/la_norms.f90:2629`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2629) |
| `la_norm_4d_order_err_int_s` | function | [`src/la_norms.f90:2712`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2712) |
| `la_norm_5d_order_err_int_s` | function | [`src/la_norms.f90:2795`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2795) |
| `la_norm_6d_order_err_int_s` | function | [`src/la_norms.f90:2878`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2878) |
| `la_norm_7d_order_err_int_s` | function | [`src/la_norms.f90:2961`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L2961) |
| `la_norm_2d_to_1d_err_int_s` | function | [`src/la_norms.f90:3050`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3050) |
| `la_norm_3d_to_2d_err_int_s` | function | [`src/la_norms.f90:3146`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3146) |
| `la_norm_4d_to_3d_err_int_s` | function | [`src/la_norms.f90:3243`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3243) |
| `la_norm_5d_to_4d_err_int_s` | function | [`src/la_norms.f90:3342`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3342) |
| `la_norm_6d_to_5d_err_int_s` | function | [`src/la_norms.f90:3441`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3441) |
| `la_norm_7d_to_6d_err_int_s` | function | [`src/la_norms.f90:3542`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3542) |
| `matrix_norm_int_s` | function | [`src/la_norms.f90:3631`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3631) |
| `matrix_norm_3d_to_1d_int_s` | function | [`src/la_norms.f90:3681`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3681) |
| `matrix_norm_4d_to_2d_int_s` | function | [`src/la_norms.f90:3777`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3777) |
| `matrix_norm_5d_to_3d_int_s` | function | [`src/la_norms.f90:3874`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3874) |
| `matrix_norm_6d_to_4d_int_s` | function | [`src/la_norms.f90:3972`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L3972) |
| `matrix_norm_7d_to_5d_int_s` | function | [`src/la_norms.f90:4071`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4071) |
| `la_norm_1d_order_err_char_d` | function | [`src/la_norms.f90:4188`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4188) |
| `la_norm_2d_order_err_char_d` | function | [`src/la_norms.f90:4271`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4271) |
| `la_norm_3d_order_err_char_d` | function | [`src/la_norms.f90:4354`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4354) |
| `la_norm_4d_order_err_char_d` | function | [`src/la_norms.f90:4437`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4437) |
| `la_norm_5d_order_err_char_d` | function | [`src/la_norms.f90:4520`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4520) |
| `la_norm_6d_order_err_char_d` | function | [`src/la_norms.f90:4603`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4603) |
| `la_norm_7d_order_err_char_d` | function | [`src/la_norms.f90:4686`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4686) |
| `la_norm_2d_to_1d_err_char_d` | function | [`src/la_norms.f90:4775`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4775) |
| `la_norm_3d_to_2d_err_char_d` | function | [`src/la_norms.f90:4871`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4871) |
| `la_norm_4d_to_3d_err_char_d` | function | [`src/la_norms.f90:4968`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L4968) |
| `la_norm_5d_to_4d_err_char_d` | function | [`src/la_norms.f90:5067`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5067) |
| `la_norm_6d_to_5d_err_char_d` | function | [`src/la_norms.f90:5166`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5166) |
| `la_norm_7d_to_6d_err_char_d` | function | [`src/la_norms.f90:5267`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5267) |
| `matrix_norm_char_d` | function | [`src/la_norms.f90:5356`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5356) |
| `matrix_norm_3d_to_1d_char_d` | function | [`src/la_norms.f90:5406`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5406) |
| `matrix_norm_4d_to_2d_char_d` | function | [`src/la_norms.f90:5502`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5502) |
| `matrix_norm_5d_to_3d_char_d` | function | [`src/la_norms.f90:5599`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5599) |
| `matrix_norm_6d_to_4d_char_d` | function | [`src/la_norms.f90:5697`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5697) |
| `matrix_norm_7d_to_5d_char_d` | function | [`src/la_norms.f90:5796`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5796) |
| `la_norm_1d_order_err_int_d` | function | [`src/la_norms.f90:5913`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5913) |
| `la_norm_2d_order_err_int_d` | function | [`src/la_norms.f90:5996`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L5996) |
| `la_norm_3d_order_err_int_d` | function | [`src/la_norms.f90:6079`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6079) |
| `la_norm_4d_order_err_int_d` | function | [`src/la_norms.f90:6162`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6162) |
| `la_norm_5d_order_err_int_d` | function | [`src/la_norms.f90:6245`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6245) |
| `la_norm_6d_order_err_int_d` | function | [`src/la_norms.f90:6328`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6328) |
| `la_norm_7d_order_err_int_d` | function | [`src/la_norms.f90:6411`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6411) |
| `la_norm_2d_to_1d_err_int_d` | function | [`src/la_norms.f90:6500`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6500) |
| `la_norm_3d_to_2d_err_int_d` | function | [`src/la_norms.f90:6596`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6596) |
| `la_norm_4d_to_3d_err_int_d` | function | [`src/la_norms.f90:6693`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6693) |
| `la_norm_5d_to_4d_err_int_d` | function | [`src/la_norms.f90:6792`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6792) |
| `la_norm_6d_to_5d_err_int_d` | function | [`src/la_norms.f90:6891`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6891) |
| `la_norm_7d_to_6d_err_int_d` | function | [`src/la_norms.f90:6992`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L6992) |
| `matrix_norm_int_d` | function | [`src/la_norms.f90:7081`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7081) |
| `matrix_norm_3d_to_1d_int_d` | function | [`src/la_norms.f90:7131`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7131) |
| `matrix_norm_4d_to_2d_int_d` | function | [`src/la_norms.f90:7227`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7227) |
| `matrix_norm_5d_to_3d_int_d` | function | [`src/la_norms.f90:7324`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7324) |
| `matrix_norm_6d_to_4d_int_d` | function | [`src/la_norms.f90:7422`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7422) |
| `matrix_norm_7d_to_5d_int_d` | function | [`src/la_norms.f90:7521`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7521) |
| `la_norm_1d_order_err_char_q` | function | [`src/la_norms.f90:7638`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7638) |
| `la_norm_2d_order_err_char_q` | function | [`src/la_norms.f90:7721`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7721) |
| `la_norm_3d_order_err_char_q` | function | [`src/la_norms.f90:7804`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7804) |
| `la_norm_4d_order_err_char_q` | function | [`src/la_norms.f90:7887`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7887) |
| `la_norm_5d_order_err_char_q` | function | [`src/la_norms.f90:7970`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L7970) |
| `la_norm_6d_order_err_char_q` | function | [`src/la_norms.f90:8053`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8053) |
| `la_norm_7d_order_err_char_q` | function | [`src/la_norms.f90:8136`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8136) |
| `la_norm_2d_to_1d_err_char_q` | function | [`src/la_norms.f90:8225`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8225) |
| `la_norm_3d_to_2d_err_char_q` | function | [`src/la_norms.f90:8321`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8321) |
| `la_norm_4d_to_3d_err_char_q` | function | [`src/la_norms.f90:8418`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8418) |
| `la_norm_5d_to_4d_err_char_q` | function | [`src/la_norms.f90:8517`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8517) |
| `la_norm_6d_to_5d_err_char_q` | function | [`src/la_norms.f90:8616`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8616) |
| `la_norm_7d_to_6d_err_char_q` | function | [`src/la_norms.f90:8717`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8717) |
| `matrix_norm_char_q` | function | [`src/la_norms.f90:8806`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8806) |
| `matrix_norm_3d_to_1d_char_q` | function | [`src/la_norms.f90:8856`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8856) |
| `matrix_norm_4d_to_2d_char_q` | function | [`src/la_norms.f90:8952`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L8952) |
| `matrix_norm_5d_to_3d_char_q` | function | [`src/la_norms.f90:9049`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9049) |
| `matrix_norm_6d_to_4d_char_q` | function | [`src/la_norms.f90:9147`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9147) |
| `matrix_norm_7d_to_5d_char_q` | function | [`src/la_norms.f90:9246`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9246) |
| `la_norm_1d_order_err_int_q` | function | [`src/la_norms.f90:9363`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9363) |
| `la_norm_2d_order_err_int_q` | function | [`src/la_norms.f90:9446`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9446) |
| `la_norm_3d_order_err_int_q` | function | [`src/la_norms.f90:9529`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9529) |
| `la_norm_4d_order_err_int_q` | function | [`src/la_norms.f90:9612`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9612) |
| `la_norm_5d_order_err_int_q` | function | [`src/la_norms.f90:9695`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9695) |
| `la_norm_6d_order_err_int_q` | function | [`src/la_norms.f90:9778`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9778) |
| `la_norm_7d_order_err_int_q` | function | [`src/la_norms.f90:9861`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9861) |
| `la_norm_2d_to_1d_err_int_q` | function | [`src/la_norms.f90:9950`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L9950) |
| `la_norm_3d_to_2d_err_int_q` | function | [`src/la_norms.f90:10046`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10046) |
| `la_norm_4d_to_3d_err_int_q` | function | [`src/la_norms.f90:10143`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10143) |
| `la_norm_5d_to_4d_err_int_q` | function | [`src/la_norms.f90:10242`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10242) |
| `la_norm_6d_to_5d_err_int_q` | function | [`src/la_norms.f90:10341`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10341) |
| `la_norm_7d_to_6d_err_int_q` | function | [`src/la_norms.f90:10442`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10442) |
| `matrix_norm_int_q` | function | [`src/la_norms.f90:10531`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10531) |
| `matrix_norm_3d_to_1d_int_q` | function | [`src/la_norms.f90:10581`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10581) |
| `matrix_norm_4d_to_2d_int_q` | function | [`src/la_norms.f90:10677`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10677) |
| `matrix_norm_5d_to_3d_int_q` | function | [`src/la_norms.f90:10774`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10774) |
| `matrix_norm_6d_to_4d_int_q` | function | [`src/la_norms.f90:10872`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10872) |
| `matrix_norm_7d_to_5d_int_q` | function | [`src/la_norms.f90:10971`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L10971) |
| `la_norm_1d_order_err_char_c` | function | [`src/la_norms.f90:11088`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11088) |
| `la_norm_2d_order_err_char_c` | function | [`src/la_norms.f90:11171`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11171) |
| `la_norm_3d_order_err_char_c` | function | [`src/la_norms.f90:11254`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11254) |
| `la_norm_4d_order_err_char_c` | function | [`src/la_norms.f90:11337`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11337) |
| `la_norm_5d_order_err_char_c` | function | [`src/la_norms.f90:11420`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11420) |
| `la_norm_6d_order_err_char_c` | function | [`src/la_norms.f90:11503`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11503) |
| `la_norm_7d_order_err_char_c` | function | [`src/la_norms.f90:11586`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11586) |
| `la_norm_2d_to_1d_err_char_c` | function | [`src/la_norms.f90:11675`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11675) |
| `la_norm_3d_to_2d_err_char_c` | function | [`src/la_norms.f90:11771`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11771) |
| `la_norm_4d_to_3d_err_char_c` | function | [`src/la_norms.f90:11868`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11868) |
| `la_norm_5d_to_4d_err_char_c` | function | [`src/la_norms.f90:11967`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L11967) |
| `la_norm_6d_to_5d_err_char_c` | function | [`src/la_norms.f90:12066`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12066) |
| `la_norm_7d_to_6d_err_char_c` | function | [`src/la_norms.f90:12167`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12167) |
| `matrix_norm_char_c` | function | [`src/la_norms.f90:12256`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12256) |
| `matrix_norm_3d_to_1d_char_c` | function | [`src/la_norms.f90:12306`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12306) |
| `matrix_norm_4d_to_2d_char_c` | function | [`src/la_norms.f90:12402`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12402) |
| `matrix_norm_5d_to_3d_char_c` | function | [`src/la_norms.f90:12499`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12499) |
| `matrix_norm_6d_to_4d_char_c` | function | [`src/la_norms.f90:12597`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12597) |
| `matrix_norm_7d_to_5d_char_c` | function | [`src/la_norms.f90:12696`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12696) |
| `la_norm_1d_order_err_int_c` | function | [`src/la_norms.f90:12813`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12813) |
| `la_norm_2d_order_err_int_c` | function | [`src/la_norms.f90:12896`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12896) |
| `la_norm_3d_order_err_int_c` | function | [`src/la_norms.f90:12979`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L12979) |
| `la_norm_4d_order_err_int_c` | function | [`src/la_norms.f90:13062`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13062) |
| `la_norm_5d_order_err_int_c` | function | [`src/la_norms.f90:13145`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13145) |
| `la_norm_6d_order_err_int_c` | function | [`src/la_norms.f90:13228`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13228) |
| `la_norm_7d_order_err_int_c` | function | [`src/la_norms.f90:13311`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13311) |
| `la_norm_2d_to_1d_err_int_c` | function | [`src/la_norms.f90:13400`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13400) |
| `la_norm_3d_to_2d_err_int_c` | function | [`src/la_norms.f90:13496`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13496) |
| `la_norm_4d_to_3d_err_int_c` | function | [`src/la_norms.f90:13593`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13593) |
| `la_norm_5d_to_4d_err_int_c` | function | [`src/la_norms.f90:13692`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13692) |
| `la_norm_6d_to_5d_err_int_c` | function | [`src/la_norms.f90:13791`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13791) |
| `la_norm_7d_to_6d_err_int_c` | function | [`src/la_norms.f90:13892`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13892) |
| `matrix_norm_int_c` | function | [`src/la_norms.f90:13981`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L13981) |
| `matrix_norm_3d_to_1d_int_c` | function | [`src/la_norms.f90:14031`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14031) |
| `matrix_norm_4d_to_2d_int_c` | function | [`src/la_norms.f90:14127`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14127) |
| `matrix_norm_5d_to_3d_int_c` | function | [`src/la_norms.f90:14224`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14224) |
| `matrix_norm_6d_to_4d_int_c` | function | [`src/la_norms.f90:14322`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14322) |
| `matrix_norm_7d_to_5d_int_c` | function | [`src/la_norms.f90:14421`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14421) |
| `la_norm_1d_order_err_char_z` | function | [`src/la_norms.f90:14538`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14538) |
| `la_norm_2d_order_err_char_z` | function | [`src/la_norms.f90:14621`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14621) |
| `la_norm_3d_order_err_char_z` | function | [`src/la_norms.f90:14704`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14704) |
| `la_norm_4d_order_err_char_z` | function | [`src/la_norms.f90:14787`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14787) |
| `la_norm_5d_order_err_char_z` | function | [`src/la_norms.f90:14870`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14870) |
| `la_norm_6d_order_err_char_z` | function | [`src/la_norms.f90:14953`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L14953) |
| `la_norm_7d_order_err_char_z` | function | [`src/la_norms.f90:15036`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15036) |
| `la_norm_2d_to_1d_err_char_z` | function | [`src/la_norms.f90:15125`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15125) |
| `la_norm_3d_to_2d_err_char_z` | function | [`src/la_norms.f90:15221`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15221) |
| `la_norm_4d_to_3d_err_char_z` | function | [`src/la_norms.f90:15318`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15318) |
| `la_norm_5d_to_4d_err_char_z` | function | [`src/la_norms.f90:15417`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15417) |
| `la_norm_6d_to_5d_err_char_z` | function | [`src/la_norms.f90:15516`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15516) |
| `la_norm_7d_to_6d_err_char_z` | function | [`src/la_norms.f90:15617`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15617) |
| `matrix_norm_char_z` | function | [`src/la_norms.f90:15706`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15706) |
| `matrix_norm_3d_to_1d_char_z` | function | [`src/la_norms.f90:15756`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15756) |
| `matrix_norm_4d_to_2d_char_z` | function | [`src/la_norms.f90:15852`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15852) |
| `matrix_norm_5d_to_3d_char_z` | function | [`src/la_norms.f90:15949`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L15949) |
| `matrix_norm_6d_to_4d_char_z` | function | [`src/la_norms.f90:16047`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16047) |
| `matrix_norm_7d_to_5d_char_z` | function | [`src/la_norms.f90:16146`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16146) |
| `la_norm_1d_order_err_int_z` | function | [`src/la_norms.f90:16263`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16263) |
| `la_norm_2d_order_err_int_z` | function | [`src/la_norms.f90:16346`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16346) |
| `la_norm_3d_order_err_int_z` | function | [`src/la_norms.f90:16429`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16429) |
| `la_norm_4d_order_err_int_z` | function | [`src/la_norms.f90:16512`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16512) |
| `la_norm_5d_order_err_int_z` | function | [`src/la_norms.f90:16595`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16595) |
| `la_norm_6d_order_err_int_z` | function | [`src/la_norms.f90:16678`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16678) |
| `la_norm_7d_order_err_int_z` | function | [`src/la_norms.f90:16761`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16761) |
| `la_norm_2d_to_1d_err_int_z` | function | [`src/la_norms.f90:16850`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16850) |
| `la_norm_3d_to_2d_err_int_z` | function | [`src/la_norms.f90:16946`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L16946) |
| `la_norm_4d_to_3d_err_int_z` | function | [`src/la_norms.f90:17043`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17043) |
| `la_norm_5d_to_4d_err_int_z` | function | [`src/la_norms.f90:17142`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17142) |
| `la_norm_6d_to_5d_err_int_z` | function | [`src/la_norms.f90:17241`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17241) |
| `la_norm_7d_to_6d_err_int_z` | function | [`src/la_norms.f90:17342`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17342) |
| `matrix_norm_int_z` | function | [`src/la_norms.f90:17431`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17431) |
| `matrix_norm_3d_to_1d_int_z` | function | [`src/la_norms.f90:17481`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17481) |
| `matrix_norm_4d_to_2d_int_z` | function | [`src/la_norms.f90:17577`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17577) |
| `matrix_norm_5d_to_3d_int_z` | function | [`src/la_norms.f90:17674`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17674) |
| `matrix_norm_6d_to_4d_int_z` | function | [`src/la_norms.f90:17772`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17772) |
| `matrix_norm_7d_to_5d_int_z` | function | [`src/la_norms.f90:17871`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17871) |
| `la_norm_1d_order_err_char_w` | function | [`src/la_norms.f90:17988`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L17988) |
| `la_norm_2d_order_err_char_w` | function | [`src/la_norms.f90:18071`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18071) |
| `la_norm_3d_order_err_char_w` | function | [`src/la_norms.f90:18154`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18154) |
| `la_norm_4d_order_err_char_w` | function | [`src/la_norms.f90:18237`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18237) |
| `la_norm_5d_order_err_char_w` | function | [`src/la_norms.f90:18320`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18320) |
| `la_norm_6d_order_err_char_w` | function | [`src/la_norms.f90:18403`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18403) |
| `la_norm_7d_order_err_char_w` | function | [`src/la_norms.f90:18486`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18486) |
| `la_norm_2d_to_1d_err_char_w` | function | [`src/la_norms.f90:18575`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18575) |
| `la_norm_3d_to_2d_err_char_w` | function | [`src/la_norms.f90:18671`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18671) |
| `la_norm_4d_to_3d_err_char_w` | function | [`src/la_norms.f90:18768`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18768) |
| `la_norm_5d_to_4d_err_char_w` | function | [`src/la_norms.f90:18867`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18867) |
| `la_norm_6d_to_5d_err_char_w` | function | [`src/la_norms.f90:18966`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L18966) |
| `la_norm_7d_to_6d_err_char_w` | function | [`src/la_norms.f90:19067`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19067) |
| `matrix_norm_char_w` | function | [`src/la_norms.f90:19156`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19156) |
| `matrix_norm_3d_to_1d_char_w` | function | [`src/la_norms.f90:19206`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19206) |
| `matrix_norm_4d_to_2d_char_w` | function | [`src/la_norms.f90:19302`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19302) |
| `matrix_norm_5d_to_3d_char_w` | function | [`src/la_norms.f90:19399`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19399) |
| `matrix_norm_6d_to_4d_char_w` | function | [`src/la_norms.f90:19497`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19497) |
| `matrix_norm_7d_to_5d_char_w` | function | [`src/la_norms.f90:19596`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19596) |
| `la_norm_1d_order_err_int_w` | function | [`src/la_norms.f90:19713`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19713) |
| `la_norm_2d_order_err_int_w` | function | [`src/la_norms.f90:19796`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19796) |
| `la_norm_3d_order_err_int_w` | function | [`src/la_norms.f90:19879`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19879) |
| `la_norm_4d_order_err_int_w` | function | [`src/la_norms.f90:19962`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L19962) |
| `la_norm_5d_order_err_int_w` | function | [`src/la_norms.f90:20045`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20045) |
| `la_norm_6d_order_err_int_w` | function | [`src/la_norms.f90:20128`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20128) |
| `la_norm_7d_order_err_int_w` | function | [`src/la_norms.f90:20211`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20211) |
| `la_norm_2d_to_1d_err_int_w` | function | [`src/la_norms.f90:20300`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20300) |
| `la_norm_3d_to_2d_err_int_w` | function | [`src/la_norms.f90:20396`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20396) |
| `la_norm_4d_to_3d_err_int_w` | function | [`src/la_norms.f90:20493`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20493) |
| `la_norm_5d_to_4d_err_int_w` | function | [`src/la_norms.f90:20592`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20592) |
| `la_norm_6d_to_5d_err_int_w` | function | [`src/la_norms.f90:20691`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20691) |
| `la_norm_7d_to_6d_err_int_w` | function | [`src/la_norms.f90:20792`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20792) |
| `matrix_norm_int_w` | function | [`src/la_norms.f90:20881`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20881) |
| `matrix_norm_3d_to_1d_int_w` | function | [`src/la_norms.f90:20931`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L20931) |
| `matrix_norm_4d_to_2d_int_w` | function | [`src/la_norms.f90:21027`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L21027) |
| `matrix_norm_5d_to_3d_int_w` | function | [`src/la_norms.f90:21124`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L21124) |
| `matrix_norm_6d_to_4d_int_w` | function | [`src/la_norms.f90:21222`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L21222) |
| `matrix_norm_7d_to_5d_int_w` | function | [`src/la_norms.f90:21321`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_norms.f90#L21321) |
| `la_pseudoinvert_s` | subroutine | [`src/la_pinv.f90:172`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L172) |
| `la_pseudoinvert_d` | subroutine | [`src/la_pinv.f90:271`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L271) |
| `la_pseudoinvert_q` | subroutine | [`src/la_pinv.f90:370`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L370) |
| `la_pseudoinvert_c` | subroutine | [`src/la_pinv.f90:469`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L469) |
| `la_pseudoinvert_z` | subroutine | [`src/la_pinv.f90:568`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L568) |
| `la_pseudoinvert_w` | subroutine | [`src/la_pinv.f90:667`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_pinv.f90#L667) |
| `get_schur_s_workspace` | subroutine | [`src/la_schur.f90:144`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L144) |
| `get_schur_q_workspace` | subroutine | [`src/la_schur.f90:648`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L648) |
| `get_schur_c_workspace` | subroutine | [`src/la_schur.f90:900`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L900) |
| `get_schur_w_workspace` | subroutine | [`src/la_schur.f90:1400`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_schur.f90#L1400) |
| `la_ssolve_one` | function | [`src/la_solve.f90:272`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L272) |
| `la_dsolve_one` | function | [`src/la_solve.f90:576`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L576) |
| `la_qsolve_one` | function | [`src/la_solve.f90:880`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L880) |
| `la_csolve_one` | function | [`src/la_solve.f90:1184`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L1184) |
| `la_zsolve_one` | function | [`src/la_solve.f90:1488`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L1488) |
| `la_wsolve_one` | function | [`src/la_solve.f90:1792`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L1792) |
| `la_ssolve_multiple` | function | [`src/la_solve.f90:2096`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L2096) |
| `la_dsolve_multiple` | function | [`src/la_solve.f90:2400`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L2400) |
| `la_qsolve_multiple` | function | [`src/la_solve.f90:2704`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L2704) |
| `la_csolve_multiple` | function | [`src/la_solve.f90:3008`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L3008) |
| `la_zsolve_multiple` | function | [`src/la_solve.f90:3312`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L3312) |
| `la_wsolve_multiple` | function | [`src/la_solve.f90:3616`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_solve.f90#L3616) |
| `la_svd_s` | subroutine | [`src/la_svd.f90:141`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L141) |
| `la_svd_d` | subroutine | [`src/la_svd.f90:328`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L328) |
| `la_svd_q` | subroutine | [`src/la_svd.f90:515`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L515) |
| `la_svd_c` | subroutine | [`src/la_svd.f90:702`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L702) |
| `la_svd_z` | subroutine | [`src/la_svd.f90:895`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L895) |
| `la_svd_w` | subroutine | [`src/la_svd.f90:1088`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_svd.f90#L1088) |

## Non-pure interface declarations

These declarations are kept separate because they may describe external implementations rather than code defined in this repository.

| Procedure | Kind | Source |
|---|---|---|
| `cgees` | subroutine | [`src/la_lapack.F90:1270`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1270) |
| `dgees` | subroutine | [`src/la_lapack.F90:1287`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1287) |
| `sgees` | subroutine | [`src/la_lapack.F90:1304`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1304) |
| `zgees` | subroutine | [`src/la_lapack.F90:1321`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1321) |
| `cgeesx` | subroutine | [`src/la_lapack.F90:1360`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1360) |
| `dgeesx` | subroutine | [`src/la_lapack.F90:1377`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1377) |
| `sgeesx` | subroutine | [`src/la_lapack.F90:1394`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1394) |
| `zgeesx` | subroutine | [`src/la_lapack.F90:1411`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1411) |
| `cgeev` | subroutine | [`src/la_lapack.F90:1441`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1441) |
| `dgeev` | subroutine | [`src/la_lapack.F90:1456`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1456) |
| `sgeev` | subroutine | [`src/la_lapack.F90:1471`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1471) |
| `zgeev` | subroutine | [`src/la_lapack.F90:1486`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1486) |
| `cgeevx` | subroutine | [`src/la_lapack.F90:1529`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1529) |
| `dgeevx` | subroutine | [`src/la_lapack.F90:1544`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1544) |
| `sgeevx` | subroutine | [`src/la_lapack.F90:1560`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1560) |
| `zgeevx` | subroutine | [`src/la_lapack.F90:1576`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1576) |
| `cgels` | subroutine | [`src/la_lapack.F90:1970`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1970) |
| `dgels` | subroutine | [`src/la_lapack.F90:1983`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1983) |
| `sgels` | subroutine | [`src/la_lapack.F90:1997`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L1997) |
| `zgels` | subroutine | [`src/la_lapack.F90:2011`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2011) |
| `cgelsd` | subroutine | [`src/la_lapack.F90:2052`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2052) |
| `dgelsd` | subroutine | [`src/la_lapack.F90:2067`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2067) |
| `sgelsd` | subroutine | [`src/la_lapack.F90:2082`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2082) |
| `zgelsd` | subroutine | [`src/la_lapack.F90:2097`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2097) |
| `cgelss` | subroutine | [`src/la_lapack.F90:2127`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2127) |
| `dgelss` | subroutine | [`src/la_lapack.F90:2142`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2142) |
| `sgelss` | subroutine | [`src/la_lapack.F90:2157`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2157) |
| `zgelss` | subroutine | [`src/la_lapack.F90:2172`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2172) |
| `cgelsy` | subroutine | [`src/la_lapack.F90:2222`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2222) |
| `dgelsy` | subroutine | [`src/la_lapack.F90:2238`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2238) |
| `sgelsy` | subroutine | [`src/la_lapack.F90:2254`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2254) |
| `zgelsy` | subroutine | [`src/la_lapack.F90:2270`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2270) |
| `cgeqr2p` | subroutine | [`src/la_lapack.F90:2765`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2765) |
| `dgeqr2p` | subroutine | [`src/la_lapack.F90:2777`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2777) |
| `sgeqr2p` | subroutine | [`src/la_lapack.F90:2790`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2790) |
| `zgeqr2p` | subroutine | [`src/la_lapack.F90:2803`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2803) |
| `cgeqrfp` | subroutine | [`src/la_lapack.F90:2886`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2886) |
| `dgeqrfp` | subroutine | [`src/la_lapack.F90:2898`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2898) |
| `sgeqrfp` | subroutine | [`src/la_lapack.F90:2911`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2911) |
| `zgeqrfp` | subroutine | [`src/la_lapack.F90:2924`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L2924) |
| `cgesdd` | subroutine | [`src/la_lapack.F90:3248`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3248) |
| `dgesdd` | subroutine | [`src/la_lapack.F90:3263`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3263) |
| `sgesdd` | subroutine | [`src/la_lapack.F90:3278`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3278) |
| `zgesdd` | subroutine | [`src/la_lapack.F90:3293`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3293) |
| `cgesvd` | subroutine | [`src/la_lapack.F90:3380`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3380) |
| `dgesvd` | subroutine | [`src/la_lapack.F90:3395`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3395) |
| `sgesvd` | subroutine | [`src/la_lapack.F90:3410`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3410) |
| `zgesvd` | subroutine | [`src/la_lapack.F90:3425`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3425) |
| `cgesvdq` | subroutine | [`src/la_lapack.F90:3452`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3452) |
| `dgesvdq` | subroutine | [`src/la_lapack.F90:3468`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3468) |
| `sgesvdq` | subroutine | [`src/la_lapack.F90:3484`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3484) |
| `zgesvdq` | subroutine | [`src/la_lapack.F90:3500`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3500) |
| `cgesvx` | subroutine | [`src/la_lapack.F90:3597`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3597) |
| `dgesvx` | subroutine | [`src/la_lapack.F90:3615`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3615) |
| `sgesvx` | subroutine | [`src/la_lapack.F90:3632`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3632) |
| `zgesvx` | subroutine | [`src/la_lapack.F90:3649`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3649) |
| `cgetsls` | subroutine | [`src/la_lapack.F90:3931`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3931) |
| `dgetsls` | subroutine | [`src/la_lapack.F90:3944`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3944) |
| `sgetsls` | subroutine | [`src/la_lapack.F90:3958`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3958) |
| `zgetsls` | subroutine | [`src/la_lapack.F90:3972`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L3972) |
| `cgges` | subroutine | [`src/la_lapack.F90:4212`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4212) |
| `dgges` | subroutine | [`src/la_lapack.F90:4230`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4230) |
| `sgges` | subroutine | [`src/la_lapack.F90:4248`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4248) |
| `zgges` | subroutine | [`src/la_lapack.F90:4266`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4266) |
| `cgges3` | subroutine | [`src/la_lapack.F90:4313`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4313) |
| `dgges3` | subroutine | [`src/la_lapack.F90:4331`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4331) |
| `sgges3` | subroutine | [`src/la_lapack.F90:4349`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4349) |
| `zgges3` | subroutine | [`src/la_lapack.F90:4367`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4367) |
| `cggev` | subroutine | [`src/la_lapack.F90:4403`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4403) |
| `dggev` | subroutine | [`src/la_lapack.F90:4419`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4419) |
| `sggev` | subroutine | [`src/la_lapack.F90:4435`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4435) |
| `zggev` | subroutine | [`src/la_lapack.F90:4451`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4451) |
| `cggev3` | subroutine | [`src/la_lapack.F90:4485`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4485) |
| `dggev3` | subroutine | [`src/la_lapack.F90:4501`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4501) |
| `sggev3` | subroutine | [`src/la_lapack.F90:4517`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4517) |
| `zggev3` | subroutine | [`src/la_lapack.F90:4533`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L4533) |
| `chbev` | subroutine | [`src/la_lapack.F90:5530`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5530) |
| `zhbev` | subroutine | [`src/la_lapack.F90:5546`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5546) |
| `chbevd` | subroutine | [`src/la_lapack.F90:5573`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5573) |
| `zhbevd` | subroutine | [`src/la_lapack.F90:5589`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5589) |
| `cheev` | subroutine | [`src/la_lapack.F90:5891`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5891) |
| `zheev` | subroutine | [`src/la_lapack.F90:5906`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5906) |
| `cheevd` | subroutine | [`src/la_lapack.F90:5932`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5932) |
| `zheevd` | subroutine | [`src/la_lapack.F90:5948`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L5948) |
| `cheevr` | subroutine | [`src/la_lapack.F90:6016`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6016) |
| `zheevr` | subroutine | [`src/la_lapack.F90:6033`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6033) |
| `chegv` | subroutine | [`src/la_lapack.F90:6092`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6092) |
| `zhegv` | subroutine | [`src/la_lapack.F90:6108`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6108) |
| `chegvd` | subroutine | [`src/la_lapack.F90:6137`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6137) |
| `zhegvd` | subroutine | [`src/la_lapack.F90:6153`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L6153) |
| `chgeqz` | subroutine | [`src/la_lapack.F90:7061`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7061) |
| `dhgeqz` | subroutine | [`src/la_lapack.F90:7076`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7076) |
| `shgeqz` | subroutine | [`src/la_lapack.F90:7091`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7091) |
| `zhgeqz` | subroutine | [`src/la_lapack.F90:7106`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7106) |
| `chpev` | subroutine | [`src/la_lapack.F90:7165`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7165) |
| `zhpev` | subroutine | [`src/la_lapack.F90:7180`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7180) |
| `chpevd` | subroutine | [`src/la_lapack.F90:7206`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7206) |
| `zhpevd` | subroutine | [`src/la_lapack.F90:7222`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7222) |
| `chpgv` | subroutine | [`src/la_lapack.F90:7282`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7282) |
| `zhpgv` | subroutine | [`src/la_lapack.F90:7298`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7298) |
| `chpgvd` | subroutine | [`src/la_lapack.F90:7328`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7328) |
| `zhpgvd` | subroutine | [`src/la_lapack.F90:7344`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7344) |
| `chsein` | subroutine | [`src/la_lapack.F90:7582`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7582) |
| `dhsein` | subroutine | [`src/la_lapack.F90:7599`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7599) |
| `shsein` | subroutine | [`src/la_lapack.F90:7616`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7616) |
| `zhsein` | subroutine | [`src/la_lapack.F90:7633`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7633) |
| `dhseqr` | subroutine | [`src/la_lapack.F90:7675`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7675) |
| `shseqr` | subroutine | [`src/la_lapack.F90:7690`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7690) |
| `cla_gbamv` | subroutine | [`src/la_lapack.F90:7760`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7760) |
| `dla_gbamv` | subroutine | [`src/la_lapack.F90:7773`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7773) |
| `sla_gbamv` | subroutine | [`src/la_lapack.F90:7786`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7786) |
| `zla_gbamv` | subroutine | [`src/la_lapack.F90:7799`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7799) |
| `dla_gbrcond` | function | [`src/la_lapack.F90:7824`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7824) |
| `sla_gbrcond` | function | [`src/la_lapack.F90:7839`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7839) |
| `cla_gbrcond_c` | function | [`src/la_lapack.F90:7858`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7858) |
| `zla_gbrcond_c` | function | [`src/la_lapack.F90:7876`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7876) |
| `cla_geamv` | subroutine | [`src/la_lapack.F90:7964`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7964) |
| `dla_geamv` | subroutine | [`src/la_lapack.F90:7976`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7976) |
| `sla_geamv` | subroutine | [`src/la_lapack.F90:7988`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L7988) |
| `zla_geamv` | subroutine | [`src/la_lapack.F90:8000`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8000) |
| `dla_gercond` | function | [`src/la_lapack.F90:8024`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8024) |
| `sla_gercond` | function | [`src/la_lapack.F90:8039`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8039) |
| `cla_gercond_c` | function | [`src/la_lapack.F90:8058`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8058) |
| `zla_gercond_c` | function | [`src/la_lapack.F90:8076`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8076) |
| `cla_heamv` | subroutine | [`src/la_lapack.F90:8159`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8159) |
| `zla_heamv` | subroutine | [`src/la_lapack.F90:8172`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8172) |
| `cla_hercond_c` | function | [`src/la_lapack.F90:8189`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8189) |
| `zla_hercond_c` | function | [`src/la_lapack.F90:8207`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8207) |
| `cla_herpvgrw` | function | [`src/la_lapack.F90:8233`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8233) |
| `zla_herpvgrw` | function | [`src/la_lapack.F90:8247`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8247) |
| `dla_porcond` | function | [`src/la_lapack.F90:8328`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8328) |
| `sla_porcond` | function | [`src/la_lapack.F90:8343`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8343) |
| `cla_porcond_c` | function | [`src/la_lapack.F90:8362`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8362) |
| `zla_porcond_c` | function | [`src/la_lapack.F90:8380`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8380) |
| `cla_porpvgrw` | function | [`src/la_lapack.F90:8406`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8406) |
| `dla_porpvgrw` | function | [`src/la_lapack.F90:8418`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8418) |
| `sla_porpvgrw` | function | [`src/la_lapack.F90:8431`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8431) |
| `zla_porpvgrw` | function | [`src/la_lapack.F90:8444`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8444) |
| `cla_syamv` | subroutine | [`src/la_lapack.F90:8471`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8471) |
| `dla_syamv` | subroutine | [`src/la_lapack.F90:8483`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8483) |
| `sla_syamv` | subroutine | [`src/la_lapack.F90:8495`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8495) |
| `zla_syamv` | subroutine | [`src/la_lapack.F90:8507`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8507) |
| `dla_syrcond` | function | [`src/la_lapack.F90:8531`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8531) |
| `sla_syrcond` | function | [`src/la_lapack.F90:8546`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8546) |
| `cla_syrcond_c` | function | [`src/la_lapack.F90:8565`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8565) |
| `zla_syrcond_c` | function | [`src/la_lapack.F90:8583`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8583) |
| `cla_syrpvgrw` | function | [`src/la_lapack.F90:8609`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8609) |
| `dla_syrpvgrw` | function | [`src/la_lapack.F90:8622`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8622) |
| `sla_syrpvgrw` | function | [`src/la_lapack.F90:8636`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8636) |
| `zla_syrpvgrw` | function | [`src/la_lapack.F90:8650`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8650) |
| `clacon` | subroutine | [`src/la_lapack.F90:8833`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8833) |
| `dlacon` | subroutine | [`src/la_lapack.F90:8846`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8846) |
| `slacon` | subroutine | [`src/la_lapack.F90:8860`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8860) |
| `zlacon` | subroutine | [`src/la_lapack.F90:8874`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L8874) |
| `dlaexc` | subroutine | [`src/la_lapack.F90:9770`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L9770) |
| `slaexc` | subroutine | [`src/la_lapack.F90:9784`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L9784) |
| `clangb` | function | [`src/la_lapack.F90:10755`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10755) |
| `dlangb` | function | [`src/la_lapack.F90:10767`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10767) |
| `slangb` | function | [`src/la_lapack.F90:10780`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10780) |
| `zlangb` | function | [`src/la_lapack.F90:10793`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10793) |
| `clange` | function | [`src/la_lapack.F90:10811`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10811) |
| `dlange` | function | [`src/la_lapack.F90:10823`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10823) |
| `slange` | function | [`src/la_lapack.F90:10836`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10836) |
| `zlange` | function | [`src/la_lapack.F90:10849`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10849) |
| `clanhb` | function | [`src/la_lapack.F90:10919`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10919) |
| `zlanhb` | function | [`src/la_lapack.F90:10932`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10932) |
| `clanhe` | function | [`src/la_lapack.F90:10950`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10950) |
| `zlanhe` | function | [`src/la_lapack.F90:10963`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10963) |
| `clanhf` | function | [`src/la_lapack.F90:10981`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10981) |
| `zlanhf` | function | [`src/la_lapack.F90:10994`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L10994) |
| `clanhp` | function | [`src/la_lapack.F90:11012`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11012) |
| `zlanhp` | function | [`src/la_lapack.F90:11025`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11025) |
| `clanhs` | function | [`src/la_lapack.F90:11043`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11043) |
| `dlanhs` | function | [`src/la_lapack.F90:11055`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11055) |
| `slanhs` | function | [`src/la_lapack.F90:11068`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11068) |
| `zlanhs` | function | [`src/la_lapack.F90:11081`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11081) |
| `clansb` | function | [`src/la_lapack.F90:11130`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11130) |
| `dlansb` | function | [`src/la_lapack.F90:11142`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11142) |
| `slansb` | function | [`src/la_lapack.F90:11155`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11155) |
| `zlansb` | function | [`src/la_lapack.F90:11168`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11168) |
| `dlansf` | function | [`src/la_lapack.F90:11186`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11186) |
| `slansf` | function | [`src/la_lapack.F90:11199`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11199) |
| `clansp` | function | [`src/la_lapack.F90:11217`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11217) |
| `dlansp` | function | [`src/la_lapack.F90:11229`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11229) |
| `slansp` | function | [`src/la_lapack.F90:11242`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11242) |
| `zlansp` | function | [`src/la_lapack.F90:11255`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11255) |
| `clansy` | function | [`src/la_lapack.F90:11302`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11302) |
| `dlansy` | function | [`src/la_lapack.F90:11314`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11314) |
| `slansy` | function | [`src/la_lapack.F90:11327`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11327) |
| `zlansy` | function | [`src/la_lapack.F90:11340`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11340) |
| `clantb` | function | [`src/la_lapack.F90:11358`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11358) |
| `dlantb` | function | [`src/la_lapack.F90:11371`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11371) |
| `slantb` | function | [`src/la_lapack.F90:11384`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11384) |
| `zlantb` | function | [`src/la_lapack.F90:11398`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11398) |
| `clantp` | function | [`src/la_lapack.F90:11416`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11416) |
| `dlantp` | function | [`src/la_lapack.F90:11428`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11428) |
| `slantp` | function | [`src/la_lapack.F90:11441`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11441) |
| `zlantp` | function | [`src/la_lapack.F90:11454`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11454) |
| `clantr` | function | [`src/la_lapack.F90:11472`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11472) |
| `dlantr` | function | [`src/la_lapack.F90:11484`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11484) |
| `slantr` | function | [`src/la_lapack.F90:11497`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11497) |
| `zlantr` | function | [`src/la_lapack.F90:11510`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L11510) |
| `dlaqr0` | subroutine | [`src/la_lapack.F90:12141`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12141) |
| `slaqr0` | subroutine | [`src/la_lapack.F90:12156`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12156) |
| `dlaqr4` | subroutine | [`src/la_lapack.F90:12271`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12271) |
| `slaqr4` | subroutine | [`src/la_lapack.F90:12286`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12286) |
| `dlaqtr` | subroutine | [`src/la_lapack.F90:12576`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12576) |
| `slaqtr` | subroutine | [`src/la_lapack.F90:12591`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12591) |
| `claqz0` | subroutine | [`src/la_lapack.F90:12648`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12648) |
| `dlaqz0` | subroutine | [`src/la_lapack.F90:12663`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12663) |
| `slaqz0` | subroutine | [`src/la_lapack.F90:12678`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12678) |
| `zlaqz0` | subroutine | [`src/la_lapack.F90:12693`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L12693) |
| `clarfgp` | subroutine | [`src/la_lapack.F90:13252`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L13252) |
| `dlarfgp` | subroutine | [`src/la_lapack.F90:13263`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L13263) |
| `slarfgp` | subroutine | [`src/la_lapack.F90:13275`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L13275) |
| `zlarfgp` | subroutine | [`src/la_lapack.F90:13287`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L13287) |
| `dorbdb` | subroutine | [`src/la_lapack.F90:16388`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16388) |
| `sorbdb` | subroutine | [`src/la_lapack.F90:16405`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16405) |
| `dorbdb1` | subroutine | [`src/la_lapack.F90:16439`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16439) |
| `sorbdb1` | subroutine | [`src/la_lapack.F90:16454`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16454) |
| `dorbdb2` | subroutine | [`src/la_lapack.F90:16486`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16486) |
| `sorbdb2` | subroutine | [`src/la_lapack.F90:16501`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16501) |
| `dorbdb3` | subroutine | [`src/la_lapack.F90:16533`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16533) |
| `sorbdb3` | subroutine | [`src/la_lapack.F90:16548`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16548) |
| `dorbdb4` | subroutine | [`src/la_lapack.F90:16580`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16580) |
| `sorbdb4` | subroutine | [`src/la_lapack.F90:16595`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16595) |
| `dorcsd` | subroutine | [`src/la_lapack.F90:16709`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16709) |
| `sorcsd` | subroutine | [`src/la_lapack.F90:16728`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16728) |
| `dorcsd2by1` | subroutine | [`src/la_lapack.F90:16764`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16764) |
| `sorcsd2by1` | subroutine | [`src/la_lapack.F90:16780`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L16780) |
| `dsbev` | subroutine | [`src/la_lapack.F90:19875`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L19875) |
| `ssbev` | subroutine | [`src/la_lapack.F90:19889`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L19889) |
| `dsbevd` | subroutine | [`src/la_lapack.F90:19914`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L19914) |
| `ssbevd` | subroutine | [`src/la_lapack.F90:19929`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L19929) |
| `dspev` | subroutine | [`src/la_lapack.F90:20205`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20205) |
| `sspev` | subroutine | [`src/la_lapack.F90:20219`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20219) |
| `dspevd` | subroutine | [`src/la_lapack.F90:20244`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20244) |
| `sspevd` | subroutine | [`src/la_lapack.F90:20259`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20259) |
| `dspgv` | subroutine | [`src/la_lapack.F90:20318`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20318) |
| `sspgv` | subroutine | [`src/la_lapack.F90:20332`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20332) |
| `dspgvd` | subroutine | [`src/la_lapack.F90:20360`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20360) |
| `sspgvd` | subroutine | [`src/la_lapack.F90:20375`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L20375) |
| `dsyev` | subroutine | [`src/la_lapack.F90:21847`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21847) |
| `ssyev` | subroutine | [`src/la_lapack.F90:21861`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21861) |
| `dsyevd` | subroutine | [`src/la_lapack.F90:21888`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21888) |
| `ssyevd` | subroutine | [`src/la_lapack.F90:21903`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21903) |
| `dsyevr` | subroutine | [`src/la_lapack.F90:21970`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21970) |
| `ssyevr` | subroutine | [`src/la_lapack.F90:21986`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L21986) |
| `dsygv` | subroutine | [`src/la_lapack.F90:22046`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L22046) |
| `ssygv` | subroutine | [`src/la_lapack.F90:22061`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L22061) |
| `dsygvd` | subroutine | [`src/la_lapack.F90:22089`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L22089) |
| `ssygvd` | subroutine | [`src/la_lapack.F90:22104`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L22104) |
| `ctbcon` | subroutine | [`src/la_lapack.F90:23529`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L23529) |
| `dtbcon` | subroutine | [`src/la_lapack.F90:23544`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L23544) |
| `stbcon` | subroutine | [`src/la_lapack.F90:23559`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L23559) |
| `ztbcon` | subroutine | [`src/la_lapack.F90:23574`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L23574) |
| `ctpcon` | subroutine | [`src/la_lapack.F90:24516`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L24516) |
| `dtpcon` | subroutine | [`src/la_lapack.F90:24530`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L24530) |
| `stpcon` | subroutine | [`src/la_lapack.F90:24544`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L24544) |
| `ztpcon` | subroutine | [`src/la_lapack.F90:24558`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L24558) |
| `ctrcon` | subroutine | [`src/la_lapack.F90:25311`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25311) |
| `dtrcon` | subroutine | [`src/la_lapack.F90:25325`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25325) |
| `strcon` | subroutine | [`src/la_lapack.F90:25339`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25339) |
| `ztrcon` | subroutine | [`src/la_lapack.F90:25353`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25353) |
| `dtrexc` | subroutine | [`src/la_lapack.F90:25557`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25557) |
| `strexc` | subroutine | [`src/la_lapack.F90:25572`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25572) |
| `ctrsen` | subroutine | [`src/la_lapack.F90:25678`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25678) |
| `dtrsen` | subroutine | [`src/la_lapack.F90:25694`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25694) |
| `strsen` | subroutine | [`src/la_lapack.F90:25710`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25710) |
| `ztrsen` | subroutine | [`src/la_lapack.F90:25726`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25726) |
| `dtrsna` | subroutine | [`src/la_lapack.F90:25764`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25764) |
| `strsna` | subroutine | [`src/la_lapack.F90:25780`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25780) |
| `ctrsyl` | subroutine | [`src/la_lapack.F90:25822`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25822) |
| `dtrsyl` | subroutine | [`src/la_lapack.F90:25837`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25837) |
| `strsyl` | subroutine | [`src/la_lapack.F90:25853`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25853) |
| `ztrsyl` | subroutine | [`src/la_lapack.F90:25869`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L25869) |
| `cunbdb` | subroutine | [`src/la_lapack.F90:26197`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26197) |
| `zunbdb` | subroutine | [`src/la_lapack.F90:26215`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26215) |
| `cunbdb1` | subroutine | [`src/la_lapack.F90:26250`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26250) |
| `zunbdb1` | subroutine | [`src/la_lapack.F90:26265`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26265) |
| `cunbdb2` | subroutine | [`src/la_lapack.F90:26297`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26297) |
| `zunbdb2` | subroutine | [`src/la_lapack.F90:26312`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26312) |
| `cunbdb3` | subroutine | [`src/la_lapack.F90:26344`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26344) |
| `zunbdb3` | subroutine | [`src/la_lapack.F90:26359`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26359) |
| `cunbdb4` | subroutine | [`src/la_lapack.F90:26391`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26391) |
| `zunbdb4` | subroutine | [`src/la_lapack.F90:26407`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26407) |
| `cuncsd` | subroutine | [`src/la_lapack.F90:26522`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26522) |
| `zuncsd` | subroutine | [`src/la_lapack.F90:26542`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26542) |
| `cuncsd2by1` | subroutine | [`src/la_lapack.F90:26579`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26579) |
| `zuncsd2by1` | subroutine | [`src/la_lapack.F90:26596`](https://github.com/Beliavsky/fortran-lapack/blob/b948713966113d648c1c01d52c347c5f548c0f2e/src/la_lapack.F90#L26596) |

## Remaining implementations by file

| Source file | Count |
|---|---:|
| `src/la_norms.f90` | 228 |
| `src/la_lapack_eigv_sym.F90` | 89 |
| `src/la_eigs.f90` | 60 |
| `src/la_lapack_blas_like_mnorm.f90` | 60 |
| `src/la_least_squares.f90` | 54 |
| `src/la_lapack_eigv_gen.f90` | 52 |
| `src/la_lapack_others_sm.f90` | 24 |
| `src/la_lapack_eigv_gen3.f90` | 22 |
| `src/la_lapack_lsq.f90` | 20 |
| `src/la_lapack_solve_chol.f90` | 20 |
| `src/la_eye.f90` | 18 |
| `src/la_lapack_eigv_gen2.f90` | 18 |
| `src/la_lapack_solve_tri_comp.f90` | 18 |
| `src/la_pinv.f90` | 18 |
| `src/la_lapack_solve_ldl.f90` | 17 |
| `src/la_lapack_solve_lu.f90` | 14 |
| `src/la_inverse.f90` | 12 |
| `src/la_matrix_property_checks.f90` | 12 |
| `src/la_schur.f90` | 12 |
| `src/la_solve.f90` | 12 |
| `src/la_svd.f90` | 12 |
| `src/la_lapack_solve_chol_comp.f90` | 9 |
| `src/la_lapack_eigv_svd_drivers.f90` | 8 |
| `src/la_determinant.f90` | 6 |
| `src/la_lapack_eigv_comp.f90` | 6 |
| `src/la_lapack_solve_aux.f90` | 6 |
| `src/la_lapack_solve_lu_comp.f90` | 6 |
| `src/la_lapack_eigv_gen_aux.f90` | 4 |
| `src/la_lapack_eigv_svd_drivers2.f90` | 4 |
| `src/la_lapack_solve_ldl_comp.f90` | 3 |
