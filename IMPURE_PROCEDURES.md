# Remaining non-pure procedures

This mechanically generated audit lists procedures that are not declared `pure` or implicitly pure through `elemental`.
It is an inventory, not a claim that every listed procedure can safely be made pure.

- Repository revision: [`Beliavsky/fortran-lapack@45d2e9b11dfa`](https://github.com/Beliavsky/fortran-lapack/commit/45d2e9b11dface3fd94c2cb2dfece934aee74436)
- Scanned paths: `src`
- Implementations scanned: 3837
- Pure implementations: 3059
- Remaining non-pure implementations: 778
- Remaining non-pure interface declarations: 184

The reason detector is deliberately conservative. It recognizes direct I/O, saved state, `data` initialization, stop statements, selected impure intrinsics, and explicit calls to other non-pure implementations. Function references and procedure-pointer dispatch may require manual call-graph review.

## Procedures with mechanically detected review reasons

| Procedure | Kind | Source | Detected reason(s) |
|---|---|---|---|
| `la_eigvals_standard_s` | function | [`src/la_eigs.f90:401`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L401) | calls non-pure `la_eig_standard_s` at line 425 |
| `la_eigvals_noerr_standard_s` | function | [`src/la_eigs.f90:429`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L429) | calls non-pure `la_eig_standard_s` at line 451 |
| `la_eigvals_generalized_s` | function | [`src/la_eigs.f90:601`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L601) | calls non-pure `la_eig_generalized_s` at line 628 |
| `la_eigvals_noerr_generalized_s` | function | [`src/la_eigs.f90:632`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L632) | calls non-pure `la_eig_generalized_s` at line 657 |
| `la_eigvalsh_s` | function | [`src/la_eigs.f90:842`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L842) | calls non-pure `la_eigh_s` at line 866 |
| `la_eigvalsh_noerr_s` | function | [`src/la_eigs.f90:871`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L871) | calls non-pure `la_eigh_s` at line 893 |
| `la_eigvals_generalized_d` | function | [`src/la_eigs.f90:1211`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1211) | calls non-pure `la_eig_generalized_d` at line 1238 |
| `la_eigvals_noerr_generalized_d` | function | [`src/la_eigs.f90:1242`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1242) | calls non-pure `la_eig_generalized_d` at line 1267 |
| `la_eigvals_standard_q` | function | [`src/la_eigs.f90:1621`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1621) | calls non-pure `la_eig_standard_q` at line 1645 |
| `la_eigvals_noerr_standard_q` | function | [`src/la_eigs.f90:1649`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1649) | calls non-pure `la_eig_standard_q` at line 1671 |
| `la_eigvals_generalized_q` | function | [`src/la_eigs.f90:1821`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1821) | calls non-pure `la_eig_generalized_q` at line 1848 |
| `la_eigvals_noerr_generalized_q` | function | [`src/la_eigs.f90:1852`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1852) | calls non-pure `la_eig_generalized_q` at line 1877 |
| `la_eigvalsh_q` | function | [`src/la_eigs.f90:2062`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2062) | calls non-pure `la_eigh_q` at line 2086 |
| `la_eigvalsh_noerr_q` | function | [`src/la_eigs.f90:2091`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2091) | calls non-pure `la_eigh_q` at line 2113 |
| `la_eigvals_standard_c` | function | [`src/la_eigs.f90:2231`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2231) | calls non-pure `la_eig_standard_c` at line 2255 |
| `la_eigvals_noerr_standard_c` | function | [`src/la_eigs.f90:2259`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2259) | calls non-pure `la_eig_standard_c` at line 2281 |
| `la_eigvals_generalized_c` | function | [`src/la_eigs.f90:2420`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2420) | calls non-pure `la_eig_generalized_c` at line 2447 |
| `la_eigvals_noerr_generalized_c` | function | [`src/la_eigs.f90:2451`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2451) | calls non-pure `la_eig_generalized_c` at line 2476 |
| `la_eigvalsh_c` | function | [`src/la_eigs.f90:2650`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2650) | calls non-pure `la_eigh_c` at line 2674 |
| `la_eigvalsh_noerr_c` | function | [`src/la_eigs.f90:2679`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2679) | calls non-pure `la_eigh_c` at line 2701 |
| `la_eigvals_generalized_z` | function | [`src/la_eigs.f90:3009`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3009) | calls non-pure `la_eig_generalized_z` at line 3036 |
| `la_eigvals_noerr_generalized_z` | function | [`src/la_eigs.f90:3040`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3040) | calls non-pure `la_eig_generalized_z` at line 3065 |
| `la_eigvalsh_z` | function | [`src/la_eigs.f90:3239`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3239) | calls non-pure `la_eigh_z` at line 3263 |
| `la_eigvalsh_noerr_z` | function | [`src/la_eigs.f90:3268`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3268) | calls non-pure `la_eigh_z` at line 3290 |
| `la_eigvals_standard_w` | function | [`src/la_eigs.f90:3409`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3409) | calls non-pure `la_eig_standard_w` at line 3433 |
| `la_eigvals_noerr_standard_w` | function | [`src/la_eigs.f90:3437`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3437) | calls non-pure `la_eig_standard_w` at line 3459 |
| `la_eigvals_generalized_w` | function | [`src/la_eigs.f90:3598`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3598) | calls non-pure `la_eig_generalized_w` at line 3625 |
| `la_eigvals_noerr_generalized_w` | function | [`src/la_eigs.f90:3629`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3629) | calls non-pure `la_eig_generalized_w` at line 3654 |
| `la_eigvalsh_w` | function | [`src/la_eigs.f90:3828`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3828) | calls non-pure `la_eigh_w` at line 3852 |
| `la_eigvalsh_noerr_w` | function | [`src/la_eigs.f90:3857`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3857) | calls non-pure `la_eigh_w` at line 3879 |
| `la_real_eig_standard_s` | subroutine | [`src/la_eigs.f90:4031`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4031) | calls non-pure `la_eig_standard_s` at line 4058 |
| `la_real_eig_generalized_s` | subroutine | [`src/la_eigs.f90:4074`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4074) | calls non-pure `la_eig_generalized_s` at line 4105 |
| `la_real_eig_generalized_d` | subroutine | [`src/la_eigs.f90:4197`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4197) | calls non-pure `la_eig_generalized_d` at line 4228 |
| `la_real_eig_standard_q` | subroutine | [`src/la_eigs.f90:4277`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4277) | calls non-pure `la_eig_standard_q` at line 4304 |
| `la_real_eig_generalized_q` | subroutine | [`src/la_eigs.f90:4320`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4320) | calls non-pure `la_eig_generalized_q` at line 4351 |
| `la_clacon` | subroutine | [`src/la_lapack_c.f90:6513`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L6513) | `save` state at line 6534 |
| `la_chegv` | subroutine | [`src/la_lapack_c.f90:57321`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L57321) | calls non-pure `la_cheev` at line 57385 |
| `la_chegvx` | subroutine | [`src/la_lapack_c.f90:57423`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L57423) | calls non-pure `la_cheevx` at line 57512 |
| `la_chpgv` | subroutine | [`src/la_lapack_c.f90:58961`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L58961) | calls non-pure `la_chpev` at line 59008 |
| `la_chpgvx` | subroutine | [`src/la_lapack_c.f90:59048`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L59048) | calls non-pure `la_chpevx` at line 59120 |
| `la_ctrsen` | subroutine | [`src/la_lapack_c.f90:62297`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L62297) | calls non-pure `la_ctrsyl` at line 62386; calls non-pure `la_ctrsyl` at line 62406; calls non-pure `la_ctrsyl` at line 62410 |
| `la_cgesvdq` | subroutine | [`src/la_lapack_c.f90:69203`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L69203) | calls non-pure `la_cgesvd` at line 69330; calls non-pure `la_cgesvd` at line 69349; calls non-pure `la_cgesvd` at line 69352; calls non-pure `la_cgesvd` at line 69372; calls non-pure `la_cgesvd` at line 69375; calls non-pure `la_cgesvd` at line 69420; calls non-pure `la_cgesvd` at line 69429; calls non-pure `la_cgesvd` at line 69442; calls non-pure `la_cgesvd` at line 69451; calls non-pure `la_cgesvd` at line 69668; calls non-pure `la_cgesvd` at line 69674; calls non-pure `la_cgesvd` at line 69695; calls non-pure `la_cgesvd` at line 69713; calls non-pure `la_cgesvd` at line 69751; calls non-pure `la_cgesvd` at line 69776; calls non-pure `la_cgesvd` at line 69797; calls non-pure `la_cgesvd` at line 69808; calls non-pure `la_cgesvd` at line 69834; calls non-pure `la_cgesvd` at line 69888; calls non-pure `la_cgesvd` at line 69934; calls non-pure `la_cgesvd` at line 69962; calls non-pure `la_cgesvd` at line 69993; calls non-pure `la_cgesvd` at line 70017 |
| `la_cgges` | subroutine | [`src/la_lapack_c.f90:70666`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L70666) | calls non-pure `la_chgeqz` at line 70836 |
| `la_cggesx` | subroutine | [`src/la_lapack_c.f90:70919`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L70919) | calls non-pure `la_chgeqz` at line 71126 |
| `la_cggev` | subroutine | [`src/la_lapack_c.f90:71221`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L71221) | calls non-pure `la_chgeqz` at line 71402 |
| `la_cggevx` | subroutine | [`src/la_lapack_c.f90:71495`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L71495) | calls non-pure `la_chgeqz` at line 71716 |
| `la_chegvd` | subroutine | [`src/la_lapack_c.f90:72863`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L72863) | calls non-pure `la_cheevd` at line 72948 |
| `la_chpgvd` | subroutine | [`src/la_lapack_c.f90:73137`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L73137) | calls non-pure `la_chpevd` at line 73218 |
| `la_cgees` | subroutine | [`src/la_lapack_c.f90:73266`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L73266) | calls non-pure `la_ctrsen` at line 73410 |
| `la_cgeesx` | subroutine | [`src/la_lapack_c.f90:73443`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L73443) | calls non-pure `la_ctrsen` at line 73602 |
| `la_cgges3` | subroutine | [`src/la_lapack_c.f90:76458`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L76458) | calls non-pure `la_claqz0` at line 76545; calls non-pure `la_claqz0` at line 76629 |
| `la_cggev3` | subroutine | [`src/la_lapack_c.f90:76703`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L76703) | calls non-pure `la_claqz0` at line 76790; calls non-pure `la_claqz0` at line 76797; calls non-pure `la_claqz0` at line 76889 |
| `la_claqz0` | subroutine | [`src/la_lapack_c.f90:79512`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L79512) | calls non-pure `la_chgeqz` at line 79613; calls non-pure `la_claqz2` at line 79620; calls non-pure `la_claqz2` at line 79779; calls non-pure `la_chgeqz` at line 79818 |
| `la_claqz2` | subroutine | [`src/la_lapack_c.f90:79825`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L79825) | calls non-pure `la_claqz0` at line 79855; calls non-pure `la_claqz0` at line 79897 |
| `la_dlacon` | subroutine | [`src/la_lapack_d.f90:1563`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L1563) | `save` state at line 1585 |
| `la_dspgv` | subroutine | [`src/la_lapack_d.f90:55854`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L55854) | calls non-pure `la_dspev` at line 55900 |
| `la_dspgvx` | subroutine | [`src/la_lapack_d.f90:55940`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L55940) | calls non-pure `la_dspevx` at line 56012 |
| `la_dgges` | subroutine | [`src/la_lapack_d.f90:63683`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L63683) | calls non-pure `la_dhgeqz` at line 63858 |
| `la_dggesx` | subroutine | [`src/la_lapack_d.f90:64004`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L64004) | calls non-pure `la_dhgeqz` at line 64210 |
| `la_dggev` | subroutine | [`src/la_lapack_d.f90:64361`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L64361) | calls non-pure `la_dhgeqz` at line 64538 |
| `la_dggevx` | subroutine | [`src/la_lapack_d.f90:64664`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L64664) | calls non-pure `la_dhgeqz` at line 64883 |
| `la_dspgvd` | subroutine | [`src/la_lapack_d.f90:72251`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L72251) | calls non-pure `la_dspevd` at line 72325 |
| `la_dgges3` | subroutine | [`src/la_lapack_d.f90:79077`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L79077) | calls non-pure `la_dlaqz0` at line 79165; calls non-pure `la_dlaqz0` at line 79249 |
| `la_dggev3` | subroutine | [`src/la_lapack_d.f90:79380`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L79380) | calls non-pure `la_dlaqz0` at line 79462; calls non-pure `la_dlaqz0` at line 79469; calls non-pure `la_dlaqz0` at line 79561 |
| `la_dlaqz0` | subroutine | [`src/la_lapack_d.f90:81366`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L81366) | calls non-pure `la_dhgeqz` at line 81465; calls non-pure `la_dlaqz3` at line 81472; calls non-pure `la_dlaqz3` at line 81642; calls non-pure `la_dhgeqz` at line 81704 |
| `la_dlaqz3` | subroutine | [`src/la_lapack_d.f90:81711`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L81711) | calls non-pure `la_dlaqz0` at line 81743; calls non-pure `la_dlaqz0` at line 81786 |
| `la_qgees` | subroutine | [`src/la_lapack_q.f90:4348`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L4348) | calls non-pure `la_qhseqr` at line 4408; calls non-pure `la_qhseqr` at line 4475; calls non-pure `la_qtrsen` at line 4489 |
| `la_qgeesx` | subroutine | [`src/la_lapack_q.f90:4600`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L4600) | calls non-pure `la_qhseqr` at line 4674; calls non-pure `la_qhseqr` at line 4747; calls non-pure `la_qtrsen` at line 4765 |
| `la_qgeev` | subroutine | [`src/la_lapack_q.f90:4885`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L4885) | calls non-pure `la_qhseqr` at line 4948; calls non-pure `la_qhseqr` at line 4961; calls non-pure `la_qhseqr` at line 4972; calls non-pure `la_qhseqr` at line 5032; calls non-pure `la_qhseqr` at line 5052; calls non-pure `la_qhseqr` at line 5058 |
| `la_qgeevx` | subroutine | [`src/la_lapack_q.f90:5159`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L5159) | calls non-pure `la_qhseqr` at line 5236; calls non-pure `la_qhseqr` at line 5243; calls non-pure `la_qhseqr` at line 5247; calls non-pure `la_qhseqr` at line 5250; calls non-pure `la_qhseqr` at line 5331; calls non-pure `la_qhseqr` at line 5351; calls non-pure `la_qhseqr` at line 5363; calls non-pure `la_qtrsna` at line 5377 |
| `la_qgesvdq` | subroutine | [`src/la_lapack_q.f90:13365`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L13365) | calls non-pure `la_qgesvd` at line 13495; calls non-pure `la_qgesvd` at line 13514; calls non-pure `la_qgesvd` at line 13517; calls non-pure `la_qgesvd` at line 13537; calls non-pure `la_qgesvd` at line 13540; calls non-pure `la_qgesvd` at line 13585; calls non-pure `la_qgesvd` at line 13594; calls non-pure `la_qgesvd` at line 13607; calls non-pure `la_qgesvd` at line 13616; calls non-pure `la_qgesvd` at line 13833; calls non-pure `la_qgesvd` at line 13838; calls non-pure `la_qgesvd` at line 13858; calls non-pure `la_qgesvd` at line 13875; calls non-pure `la_qgesvd` at line 13912; calls non-pure `la_qgesvd` at line 13936; calls non-pure `la_qgesvd` at line 13956; calls non-pure `la_qgesvd` at line 13967; calls non-pure `la_qgesvd` at line 13991; calls non-pure `la_qgesvd` at line 14042; calls non-pure `la_qgesvd` at line 14086; calls non-pure `la_qgesvd` at line 14114; calls non-pure `la_qgesvd` at line 14144; calls non-pure `la_qgesvd` at line 14167 |
| `la_qgges` | subroutine | [`src/la_lapack_q.f90:16725`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L16725) | calls non-pure `la_qhgeqz` at line 16900 |
| `la_qgges3` | subroutine | [`src/la_lapack_q.f90:17044`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L17044) | calls non-pure `la_qlaqz0` at line 17132; calls non-pure `la_qlaqz0` at line 17216 |
| `la_qggesx` | subroutine | [`src/la_lapack_q.f90:17360`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L17360) | calls non-pure `la_qhgeqz` at line 17566 |
| `la_qggev` | subroutine | [`src/la_lapack_q.f90:17717`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L17717) | calls non-pure `la_qhgeqz` at line 17894 |
| `la_qggev3` | subroutine | [`src/la_lapack_q.f90:18015`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L18015) | calls non-pure `la_qlaqz0` at line 18097; calls non-pure `la_qlaqz0` at line 18104; calls non-pure `la_qlaqz0` at line 18196 |
| `la_qggevx` | subroutine | [`src/la_lapack_q.f90:18320`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L18320) | calls non-pure `la_qhgeqz` at line 18539 |
| `la_qhseqr` | subroutine | [`src/la_lapack_q.f90:22772`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L22772) | calls non-pure `la_qlaqr0` at line 22840; calls non-pure `la_qlaqr0` at line 22870; calls non-pure `la_qlaqr0` at line 22883; calls non-pure `la_qlaqr0` at line 22893 |
| `la_qlacon` | subroutine | [`src/la_lapack_q.f90:24825`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L24825) | `save` state at line 24847 |
| `la_qlaqr0` | subroutine | [`src/la_lapack_q.f90:34268`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L34268) | calls non-pure `la_qlaqr3` at line 34358; calls non-pure `la_qlaqr3` at line 34456; calls non-pure `la_qlaqr4` at line 34510 |
| `la_qlaqr2` | subroutine | [`src/la_lapack_q.f90:34700`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L34700) | calls non-pure `la_qtrexc` at line 34818; calls non-pure `la_qtrexc` at line 34835; calls non-pure `la_qtrexc` at line 34884 |
| `la_qlaqr3` | subroutine | [`src/la_lapack_q.f90:35001`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L35001) | calls non-pure `la_qlaqr4` at line 35038; calls non-pure `la_qlaqr4` at line 35095; calls non-pure `la_qtrexc` at line 35129; calls non-pure `la_qtrexc` at line 35146; calls non-pure `la_qtrexc` at line 35195 |
| `la_qlaqr4` | subroutine | [`src/la_lapack_q.f90:35317`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L35317) | calls non-pure `la_qlaqr2` at line 35407; calls non-pure `la_qlaqr2` at line 35505 |
| `la_qlaqz0` | subroutine | [`src/la_lapack_q.f90:36754`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L36754) | calls non-pure `la_qhgeqz` at line 36853; calls non-pure `la_qlaqz3` at line 36860; calls non-pure `la_qlaqz3` at line 37030; calls non-pure `la_qhgeqz` at line 37092 |
| `la_qlaqz3` | subroutine | [`src/la_lapack_q.f90:37265`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L37265) | calls non-pure `la_qlaqz0` at line 37297; calls non-pure `la_qlaqz0` at line 37340 |
| `la_qspgv` | subroutine | [`src/la_lapack_q.f90:63915`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L63915) | calls non-pure `la_qspev` at line 63961 |
| `la_qspgvd` | subroutine | [`src/la_lapack_q.f90:64006`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L64006) | calls non-pure `la_qspevd` at line 64080 |
| `la_qspgvx` | subroutine | [`src/la_lapack_q.f90:64125`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L64125) | calls non-pure `la_qspevx` at line 64197 |
| `la_qsygv` | subroutine | [`src/la_lapack_q.f90:70164`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L70164) | calls non-pure `la_qsyev` at line 70227 |
| `la_qsygvd` | subroutine | [`src/la_lapack_q.f90:70270`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L70270) | calls non-pure `la_qsyevd` at line 70347 |
| `la_qsygvx` | subroutine | [`src/la_lapack_q.f90:70386`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L70386) | calls non-pure `la_qsyevx` at line 70475 |
| `la_qtrexc` | subroutine | [`src/la_lapack_q.f90:82927`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L82927) | calls non-pure `la_qlaexc` at line 83001; calls non-pure `la_qlaexc` at line 83019; calls non-pure `la_qlaexc` at line 83027; calls non-pure `la_qlaexc` at line 83035; calls non-pure `la_qlaexc` at line 83044; calls non-pure `la_qlaexc` at line 83046; calls non-pure `la_qlaexc` at line 83063; calls non-pure `la_qlaexc` at line 83081; calls non-pure `la_qlaexc` at line 83089; calls non-pure `la_qlaexc` at line 83097; calls non-pure `la_qlaexc` at line 83106; calls non-pure `la_qlaexc` at line 83108 |
| `la_qtrsen` | subroutine | [`src/la_lapack_q.f90:83366`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L83366) | calls non-pure `la_qtrexc` at line 83484; calls non-pure `la_qtrsyl` at line 83501; calls non-pure `la_qtrsyl` at line 83521; calls non-pure `la_qtrsyl` at line 83525 |
| `la_qtrsna` | subroutine | [`src/la_lapack_q.f90:83558`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L83558) | calls non-pure `la_qtrexc` at line 83705; calls non-pure `la_qlaqtr` at line 83763; calls non-pure `la_qlaqtr` at line 83768; calls non-pure `la_qlaqtr` at line 83774; calls non-pure `la_qlaqtr` at line 83779 |
| `la_slacon` | subroutine | [`src/la_lapack_s.f90:1599`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L1599) | `save` state at line 1621 |
| `la_sspgv` | subroutine | [`src/la_lapack_s.f90:54510`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54510) | calls non-pure `la_sspev` at line 54556 |
| `la_sspgvx` | subroutine | [`src/la_lapack_s.f90:54596`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54596) | calls non-pure `la_sspevx` at line 54668 |
| `la_ssygv` | subroutine | [`src/la_lapack_s.f90:55060`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L55060) | calls non-pure `la_ssyev` at line 55123 |
| `la_ssygvx` | subroutine | [`src/la_lapack_s.f90:55161`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L55161) | calls non-pure `la_ssyevx` at line 55250 |
| `la_sgges` | subroutine | [`src/la_lapack_s.f90:61184`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L61184) | calls non-pure `la_shgeqz` at line 61359 |
| `la_sggesx` | subroutine | [`src/la_lapack_s.f90:61505`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L61505) | calls non-pure `la_shgeqz` at line 61711 |
| `la_sggev` | subroutine | [`src/la_lapack_s.f90:61862`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L61862) | calls non-pure `la_shgeqz` at line 62039 |
| `la_sggevx` | subroutine | [`src/la_lapack_s.f90:62165`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L62165) | calls non-pure `la_shgeqz` at line 62383 |
| `la_strexc` | subroutine | [`src/la_lapack_s.f90:65231`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L65231) | calls non-pure `la_slaexc` at line 65305; calls non-pure `la_slaexc` at line 65323; calls non-pure `la_slaexc` at line 65331; calls non-pure `la_slaexc` at line 65339; calls non-pure `la_slaexc` at line 65348; calls non-pure `la_slaexc` at line 65350; calls non-pure `la_slaexc` at line 65367; calls non-pure `la_slaexc` at line 65385; calls non-pure `la_slaexc` at line 65393; calls non-pure `la_slaexc` at line 65401; calls non-pure `la_slaexc` at line 65410; calls non-pure `la_slaexc` at line 65412 |
| `la_strsen` | subroutine | [`src/la_lapack_s.f90:65436`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L65436) | calls non-pure `la_strexc` at line 65554; calls non-pure `la_strsyl` at line 65571; calls non-pure `la_strsyl` at line 65591; calls non-pure `la_strsyl` at line 65595 |
| `la_strsna` | subroutine | [`src/la_lapack_s.f90:65628`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L65628) | calls non-pure `la_strexc` at line 65775; calls non-pure `la_slaqtr` at line 65833; calls non-pure `la_slaqtr` at line 65838; calls non-pure `la_slaqtr` at line 65844; calls non-pure `la_slaqtr` at line 65849 |
| `la_slaqr2` | subroutine | [`src/la_lapack_s.f90:66974`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L66974) | calls non-pure `la_strexc` at line 67092; calls non-pure `la_strexc` at line 67109; calls non-pure `la_strexc` at line 67158 |
| `la_ssygvd` | subroutine | [`src/la_lapack_s.f90:68164`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L68164) | calls non-pure `la_ssyevd` at line 68241 |
| `la_sspgvd` | subroutine | [`src/la_lapack_s.f90:68660`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L68660) | calls non-pure `la_sspevd` at line 68734 |
| `la_sgees` | subroutine | [`src/la_lapack_s.f90:69502`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L69502) | calls non-pure `la_shseqr` at line 69562; calls non-pure `la_shseqr` at line 69629; calls non-pure `la_strsen` at line 69643 |
| `la_sgeesx` | subroutine | [`src/la_lapack_s.f90:69754`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L69754) | calls non-pure `la_shseqr` at line 69828; calls non-pure `la_shseqr` at line 69901; calls non-pure `la_strsen` at line 69919 |
| `la_sgeev` | subroutine | [`src/la_lapack_s.f90:70039`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L70039) | calls non-pure `la_shseqr` at line 70102; calls non-pure `la_shseqr` at line 70115; calls non-pure `la_shseqr` at line 70126; calls non-pure `la_shseqr` at line 70186; calls non-pure `la_shseqr` at line 70206; calls non-pure `la_shseqr` at line 70212 |
| `la_sgeevx` | subroutine | [`src/la_lapack_s.f90:70313`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L70313) | calls non-pure `la_shseqr` at line 70390; calls non-pure `la_shseqr` at line 70397; calls non-pure `la_shseqr` at line 70401; calls non-pure `la_shseqr` at line 70404; calls non-pure `la_shseqr` at line 70485; calls non-pure `la_shseqr` at line 70505; calls non-pure `la_shseqr` at line 70517; calls non-pure `la_strsna` at line 70531 |
| `la_sgesvdq` | subroutine | [`src/la_lapack_s.f90:75695`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L75695) | calls non-pure `la_sgesvd` at line 75826; calls non-pure `la_sgesvd` at line 75845; calls non-pure `la_sgesvd` at line 75848; calls non-pure `la_sgesvd` at line 75868; calls non-pure `la_sgesvd` at line 75871; calls non-pure `la_sgesvd` at line 75916; calls non-pure `la_sgesvd` at line 75925; calls non-pure `la_sgesvd` at line 75938; calls non-pure `la_sgesvd` at line 75947; calls non-pure `la_sgesvd` at line 76164; calls non-pure `la_sgesvd` at line 76169; calls non-pure `la_sgesvd` at line 76189; calls non-pure `la_sgesvd` at line 76206; calls non-pure `la_sgesvd` at line 76243; calls non-pure `la_sgesvd` at line 76267; calls non-pure `la_sgesvd` at line 76287; calls non-pure `la_sgesvd` at line 76298; calls non-pure `la_sgesvd` at line 76322; calls non-pure `la_sgesvd` at line 76373; calls non-pure `la_sgesvd` at line 76417; calls non-pure `la_sgesvd` at line 76445; calls non-pure `la_sgesvd` at line 76475; calls non-pure `la_sgesvd` at line 76498 |
| `la_sgges3` | subroutine | [`src/la_lapack_s.f90:77556`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L77556) | calls non-pure `la_slaqz0` at line 77644; calls non-pure `la_slaqz0` at line 77728 |
| `la_sggev3` | subroutine | [`src/la_lapack_s.f90:77859`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L77859) | calls non-pure `la_slaqz0` at line 77939; calls non-pure `la_slaqz0` at line 77943; calls non-pure `la_slaqz0` at line 78035 |
| `la_shseqr` | subroutine | [`src/la_lapack_s.f90:79226`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L79226) | calls non-pure `la_slaqr0` at line 79294; calls non-pure `la_slaqr0` at line 79324; calls non-pure `la_slaqr0` at line 79337; calls non-pure `la_slaqr0` at line 79347 |
| `la_slaqr0` | subroutine | [`src/la_lapack_s.f90:79829`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L79829) | calls non-pure `la_slaqr3` at line 79919; calls non-pure `la_slaqr3` at line 80017; calls non-pure `la_slaqr4` at line 80071 |
| `la_slaqr3` | subroutine | [`src/la_lapack_s.f90:80199`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L80199) | calls non-pure `la_slaqr4` at line 80236; calls non-pure `la_slaqr4` at line 80293; calls non-pure `la_strexc` at line 80327; calls non-pure `la_strexc` at line 80344; calls non-pure `la_strexc` at line 80393 |
| `la_slaqr4` | subroutine | [`src/la_lapack_s.f90:80515`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L80515) | calls non-pure `la_slaqr2` at line 80605; calls non-pure `la_slaqr2` at line 80703 |
| `la_slaqz0` | subroutine | [`src/la_lapack_s.f90:80919`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L80919) | calls non-pure `la_shgeqz` at line 81018; calls non-pure `la_slaqz3` at line 81025; calls non-pure `la_slaqz3` at line 81195; calls non-pure `la_shgeqz` at line 81257 |
| `la_slaqz3` | subroutine | [`src/la_lapack_s.f90:81264`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L81264) | calls non-pure `la_slaqz0` at line 81296; calls non-pure `la_slaqz0` at line 81339 |
| `la_wgees` | subroutine | [`src/la_lapack_w.f90:4502`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L4502) | calls non-pure `la_wtrsen` at line 4646 |
| `la_wgeesx` | subroutine | [`src/la_lapack_w.f90:4679`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L4679) | calls non-pure `la_wtrsen` at line 4838 |
| `la_wgesvdq` | subroutine | [`src/la_lapack_w.f90:14398`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L14398) | calls non-pure `la_wgesvd` at line 14524; calls non-pure `la_wgesvd` at line 14543; calls non-pure `la_wgesvd` at line 14546; calls non-pure `la_wgesvd` at line 14566; calls non-pure `la_wgesvd` at line 14569; calls non-pure `la_wgesvd` at line 14614; calls non-pure `la_wgesvd` at line 14623; calls non-pure `la_wgesvd` at line 14636; calls non-pure `la_wgesvd` at line 14645; calls non-pure `la_wgesvd` at line 14862; calls non-pure `la_wgesvd` at line 14868; calls non-pure `la_wgesvd` at line 14889; calls non-pure `la_wgesvd` at line 14907; calls non-pure `la_wgesvd` at line 14945; calls non-pure `la_wgesvd` at line 14970; calls non-pure `la_wgesvd` at line 14991; calls non-pure `la_wgesvd` at line 15002; calls non-pure `la_wgesvd` at line 15028; calls non-pure `la_wgesvd` at line 15082; calls non-pure `la_wgesvd` at line 15128; calls non-pure `la_wgesvd` at line 15156; calls non-pure `la_wgesvd` at line 15187; calls non-pure `la_wgesvd` at line 15211 |
| `la_wgges` | subroutine | [`src/la_lapack_w.f90:17647`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L17647) | calls non-pure `la_whgeqz` at line 17817 |
| `la_wgges3` | subroutine | [`src/la_lapack_w.f90:17898`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L17898) | calls non-pure `la_wlaqz0` at line 17985; calls non-pure `la_wlaqz0` at line 18069 |
| `la_wggesx` | subroutine | [`src/la_lapack_w.f90:18150`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L18150) | calls non-pure `la_whgeqz` at line 18357 |
| `la_wggev` | subroutine | [`src/la_lapack_w.f90:18452`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L18452) | calls non-pure `la_whgeqz` at line 18633 |
| `la_wggev3` | subroutine | [`src/la_lapack_w.f90:18721`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L18721) | calls non-pure `la_wlaqz0` at line 18808; calls non-pure `la_wlaqz0` at line 18815; calls non-pure `la_wlaqz0` at line 18907 |
| `la_wggevx` | subroutine | [`src/la_lapack_w.f90:18997`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L18997) | calls non-pure `la_whgeqz` at line 19218 |
| `la_whegv` | subroutine | [`src/la_lapack_w.f90:25906`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L25906) | calls non-pure `la_wheev` at line 25970 |
| `la_whegvd` | subroutine | [`src/la_lapack_w.f90:26013`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L26013) | calls non-pure `la_wheevd` at line 26098 |
| `la_whegvx` | subroutine | [`src/la_lapack_w.f90:26140`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L26140) | calls non-pure `la_wheevx` at line 26229 |
| `la_whpgv` | subroutine | [`src/la_lapack_w.f90:32434`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L32434) | calls non-pure `la_whpev` at line 32481 |
| `la_whpgvd` | subroutine | [`src/la_lapack_w.f90:32526`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L32526) | calls non-pure `la_whpevd` at line 32607 |
| `la_whpgvx` | subroutine | [`src/la_lapack_w.f90:32654`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L32654) | calls non-pure `la_whpevx` at line 32726 |
| `la_wlacon` | subroutine | [`src/la_lapack_w.f90:36763`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L36763) | `save` state at line 36784 |
| `la_wlaqz0` | subroutine | [`src/la_lapack_w.f90:47561`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L47561) | calls non-pure `la_whgeqz` at line 47662; calls non-pure `la_wlaqz2` at line 47669; calls non-pure `la_wlaqz2` at line 47828; calls non-pure `la_whgeqz` at line 47867 |
| `la_wlaqz2` | subroutine | [`src/la_lapack_w.f90:47927`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L47927) | calls non-pure `la_wlaqz0` at line 47957; calls non-pure `la_wlaqz0` at line 47999 |
| `la_wtrsen` | subroutine | [`src/la_lapack_w.f90:74617`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L74617) | calls non-pure `la_wtrsyl` at line 74706; calls non-pure `la_wtrsyl` at line 74726; calls non-pure `la_wtrsyl` at line 74730 |
| `la_zlacon` | subroutine | [`src/la_lapack_z.f90:6610`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L6610) | `save` state at line 6631 |
| `la_zhegv` | subroutine | [`src/la_lapack_z.f90:57607`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L57607) | calls non-pure `la_zheev` at line 57671 |
| `la_zhegvx` | subroutine | [`src/la_lapack_z.f90:57709`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L57709) | calls non-pure `la_zheevx` at line 57798 |
| `la_zhpgv` | subroutine | [`src/la_lapack_z.f90:59248`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L59248) | calls non-pure `la_zhpev` at line 59295 |
| `la_zhpgvx` | subroutine | [`src/la_lapack_z.f90:59335`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L59335) | calls non-pure `la_zhpevx` at line 59407 |
| `la_zgges` | subroutine | [`src/la_lapack_z.f90:71134`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L71134) | calls non-pure `la_zhgeqz` at line 71304 |
| `la_zggesx` | subroutine | [`src/la_lapack_z.f90:71387`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L71387) | calls non-pure `la_zhgeqz` at line 71594 |
| `la_zggev` | subroutine | [`src/la_lapack_z.f90:71689`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L71689) | calls non-pure `la_zhgeqz` at line 71870 |
| `la_zggevx` | subroutine | [`src/la_lapack_z.f90:71963`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L71963) | calls non-pure `la_zhgeqz` at line 72184 |
| `la_zhegvd` | subroutine | [`src/la_lapack_z.f90:73331`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L73331) | calls non-pure `la_zheevd` at line 73416 |
| `la_zhpgvd` | subroutine | [`src/la_lapack_z.f90:73605`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L73605) | calls non-pure `la_zhpevd` at line 73686 |
| `la_zgges3` | subroutine | [`src/la_lapack_z.f90:76924`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L76924) | calls non-pure `la_zlaqz0` at line 77011; calls non-pure `la_zlaqz0` at line 77095 |
| `la_zggev3` | subroutine | [`src/la_lapack_z.f90:77169`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L77169) | calls non-pure `la_zlaqz0` at line 77256; calls non-pure `la_zlaqz0` at line 77263; calls non-pure `la_zlaqz0` at line 77355 |
| `la_zlaqz0` | subroutine | [`src/la_lapack_z.f90:79978`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L79978) | calls non-pure `la_zhgeqz` at line 80079; calls non-pure `la_zlaqz2` at line 80086; calls non-pure `la_zlaqz2` at line 80245; calls non-pure `la_zhgeqz` at line 80284 |
| `la_zlaqz2` | subroutine | [`src/la_lapack_z.f90:80291`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L80291) | calls non-pure `la_zlaqz0` at line 80321; calls non-pure `la_zlaqz0` at line 80363 |
| `la_pseudoinverse_s` | function | [`src/la_pinv.f90:238`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L238) | calls non-pure `la_pseudoinvert_s` at line 252 |
| `la_pinv_s_operator` | function | [`src/la_pinv.f90:257`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L257) | calls non-pure `la_pseudoinvert_s` at line 267 |
| `la_pseudoinverse_q` | function | [`src/la_pinv.f90:435`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L435) | calls non-pure `la_pseudoinvert_q` at line 449 |
| `la_pinv_q_operator` | function | [`src/la_pinv.f90:454`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L454) | calls non-pure `la_pseudoinvert_q` at line 464 |
| `la_pseudoinverse_c` | function | [`src/la_pinv.f90:534`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L534) | calls non-pure `la_pseudoinvert_c` at line 548 |
| `la_pinv_c_operator` | function | [`src/la_pinv.f90:553`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L553) | calls non-pure `la_pseudoinvert_c` at line 563 |
| `la_pseudoinverse_w` | function | [`src/la_pinv.f90:731`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L731) | calls non-pure `la_pseudoinvert_w` at line 745 |
| `la_pinv_w_operator` | function | [`src/la_pinv.f90:750`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L750) | calls non-pure `la_pseudoinvert_w` at line 760 |
| `la_s_schur` | subroutine | [`src/la_schur.f90:191`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L191) | calls non-pure `get_schur_s_workspace` at line 274 |
| `la_real_eig_s_schur` | subroutine | [`src/la_schur.f90:355`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L355) | calls non-pure `la_s_schur` at line 381 |
| `la_q_schur` | subroutine | [`src/la_schur.f90:695`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L695) | calls non-pure `get_schur_q_workspace` at line 778 |
| `la_real_eig_q_schur` | subroutine | [`src/la_schur.f90:859`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L859) | calls non-pure `la_q_schur` at line 885 |
| `la_c_schur` | subroutine | [`src/la_schur.f90:947`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L947) | calls non-pure `get_schur_c_workspace` at line 1030 |
| `la_real_eig_c_schur` | subroutine | [`src/la_schur.f90:1109`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L1109) | calls non-pure `la_c_schur` at line 1135 |
| `la_w_schur` | subroutine | [`src/la_schur.f90:1447`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L1447) | calls non-pure `get_schur_w_workspace` at line 1530 |
| `la_real_eig_w_schur` | subroutine | [`src/la_schur.f90:1609`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L1609) | calls non-pure `la_w_schur` at line 1635 |
| `la_svdvals_s` | function | [`src/la_svd.f90:115`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L115) | calls non-pure `la_svd_s` at line 138 |
| `la_svdvals_q` | function | [`src/la_svd.f90:489`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L489) | calls non-pure `la_svd_q` at line 512 |
| `la_svdvals_c` | function | [`src/la_svd.f90:676`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L676) | calls non-pure `la_svd_c` at line 699 |
| `la_svdvals_w` | function | [`src/la_svd.f90:1062`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L1062) | calls non-pure `la_svd_w` at line 1085 |

## Procedures requiring semantic review

No blocker recognized by this script was found. These are the best starting points for a compiler-backed purity audit, but they are not automatically proven pure.

| Procedure | Kind | Source |
|---|---|---|
| `la_sdeterminant` | function | [`src/la_determinant.f90:45`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L45) |
| `la_ddeterminant` | function | [`src/la_determinant.f90:138`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L138) |
| `la_qdeterminant` | function | [`src/la_determinant.f90:231`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L231) |
| `la_cdeterminant` | function | [`src/la_determinant.f90:324`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L324) |
| `la_zdeterminant` | function | [`src/la_determinant.f90:417`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L417) |
| `la_wdeterminant` | function | [`src/la_determinant.f90:510`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_determinant.f90#L510) |
| `la_eig_standard_s` | subroutine | [`src/la_eigs.f90:455`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L455) |
| `la_eig_generalized_s` | subroutine | [`src/la_eigs.f90:661`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L661) |
| `la_eigh_s` | subroutine | [`src/la_eigs.f90:899`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L899) |
| `la_eigvals_standard_d` | function | [`src/la_eigs.f90:1011`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1011) |
| `la_eig_generalized_d` | subroutine | [`src/la_eigs.f90:1271`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1271) |
| `la_eigvalsh_d` | function | [`src/la_eigs.f90:1452`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1452) |
| `la_eig_standard_q` | subroutine | [`src/la_eigs.f90:1675`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1675) |
| `la_eig_generalized_q` | subroutine | [`src/la_eigs.f90:1881`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L1881) |
| `la_eigh_q` | subroutine | [`src/la_eigs.f90:2119`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2119) |
| `la_eig_standard_c` | subroutine | [`src/la_eigs.f90:2285`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2285) |
| `la_eig_generalized_c` | subroutine | [`src/la_eigs.f90:2480`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2480) |
| `la_eigh_c` | subroutine | [`src/la_eigs.f90:2707`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2707) |
| `la_eigvals_standard_z` | function | [`src/la_eigs.f90:2820`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L2820) |
| `la_eig_generalized_z` | subroutine | [`src/la_eigs.f90:3069`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3069) |
| `la_eigh_z` | subroutine | [`src/la_eigs.f90:3296`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3296) |
| `la_eig_standard_w` | subroutine | [`src/la_eigs.f90:3463`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3463) |
| `la_eig_generalized_w` | subroutine | [`src/la_eigs.f90:3658`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3658) |
| `la_eigh_w` | subroutine | [`src/la_eigs.f90:3885`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L3885) |
| `la_real_eig_standard_d` | subroutine | [`src/la_eigs.f90:4154`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eigs.f90#L4154) |
| `la_eye_s_errhandle` | function | [`src/la_eye.f90:893`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L893) |
| `la_eye_d_errhandle` | function | [`src/la_eye.f90:944`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L944) |
| `la_eye_q_errhandle` | function | [`src/la_eye.f90:995`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L995) |
| `la_eye_c_errhandle` | function | [`src/la_eye.f90:1046`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1046) |
| `la_eye_z_errhandle` | function | [`src/la_eye.f90:1097`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1097) |
| `la_eye_w_errhandle` | function | [`src/la_eye.f90:1148`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1148) |
| `la_diag_s_errhandle_from_scalar` | function | [`src/la_eye.f90:1197`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1197) |
| `la_diag_s_errhandle_from_array` | function | [`src/la_eye.f90:1241`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1241) |
| `la_diag_d_errhandle_from_scalar` | function | [`src/la_eye.f90:1285`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1285) |
| `la_diag_d_errhandle_from_array` | function | [`src/la_eye.f90:1329`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1329) |
| `la_diag_q_errhandle_from_scalar` | function | [`src/la_eye.f90:1373`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1373) |
| `la_diag_q_errhandle_from_array` | function | [`src/la_eye.f90:1417`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1417) |
| `la_diag_c_errhandle_from_scalar` | function | [`src/la_eye.f90:1461`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1461) |
| `la_diag_c_errhandle_from_array` | function | [`src/la_eye.f90:1505`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1505) |
| `la_diag_z_errhandle_from_scalar` | function | [`src/la_eye.f90:1549`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1549) |
| `la_diag_z_errhandle_from_array` | function | [`src/la_eye.f90:1593`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1593) |
| `la_diag_w_errhandle_from_scalar` | function | [`src/la_eye.f90:1637`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1637) |
| `la_diag_w_errhandle_from_array` | function | [`src/la_eye.f90:1681`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_eye.f90#L1681) |
| `la_inverse_s` | function | [`src/la_inverse.f90:156`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L156) |
| `la_inverse_d` | function | [`src/la_inverse.f90:254`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L254) |
| `la_inverse_q` | function | [`src/la_inverse.f90:352`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L352) |
| `la_inverse_c` | function | [`src/la_inverse.f90:450`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L450) |
| `la_inverse_z` | function | [`src/la_inverse.f90:548`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L548) |
| `la_inverse_w` | function | [`src/la_inverse.f90:646`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_inverse.f90#L646) |
| `la_cla_porpvgrw` | function | [`src/la_lapack_c.f90:6046`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L6046) |
| `la_cla_gbrcond_c` | function | [`src/la_lapack_c.f90:38133`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38133) |
| `la_cla_gercond_c` | function | [`src/la_lapack_c.f90:38281`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38281) |
| `la_cla_hercond_c` | function | [`src/la_lapack_c.f90:38422`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38422) |
| `la_cla_herpvgrw` | function | [`src/la_lapack_c.f90:38576`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38576) |
| `la_cla_porcond_c` | function | [`src/la_lapack_c.f90:38761`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38761) |
| `la_cla_syrcond_c` | function | [`src/la_lapack_c.f90:38911`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L38911) |
| `la_cla_syrpvgrw` | function | [`src/la_lapack_c.f90:39066`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L39066) |
| `la_clangb` | function | [`src/la_lapack_c.f90:41190`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L41190) |
| `la_clange` | function | [`src/la_lapack_c.f90:41265`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L41265) |
| `la_clanhb` | function | [`src/la_lapack_c.f90:41413`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L41413) |
| `la_clanhe` | function | [`src/la_lapack_c.f90:41532`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L41532) |
| `la_clanhf` | function | [`src/la_lapack_c.f90:41642`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L41642) |
| `la_clanhp` | function | [`src/la_lapack_c.f90:42862`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L42862) |
| `la_clanhs` | function | [`src/la_lapack_c.f90:42990`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L42990) |
| `la_clansb` | function | [`src/la_lapack_c.f90:43125`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43125) |
| `la_clansp` | function | [`src/la_lapack_c.f90:43230`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43230) |
| `la_clansy` | function | [`src/la_lapack_c.f90:43363`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43363) |
| `la_clantb` | function | [`src/la_lapack_c.f90:43459`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43459) |
| `la_clantp` | function | [`src/la_lapack_c.f90:43652`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43652) |
| `la_clantr` | function | [`src/la_lapack_c.f90:43858`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L43858) |
| `la_cppsvx` | subroutine | [`src/la_lapack_c.f90:47322`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L47322) |
| `la_cspsvx` | subroutine | [`src/la_lapack_c.f90:48012`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L48012) |
| `la_csysvx` | subroutine | [`src/la_lapack_c.f90:49108`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L49108) |
| `la_ctbcon` | subroutine | [`src/la_lapack_c.f90:49205`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L49205) |
| `la_ctpcon` | subroutine | [`src/la_lapack_c.f90:50282`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L50282) |
| `la_ctrcon` | subroutine | [`src/la_lapack_c.f90:50748`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L50748) |
| `la_ctrsyl` | subroutine | [`src/la_lapack_c.f90:50855`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L50855) |
| `la_cgbsvx` | subroutine | [`src/la_lapack_c.f90:52786`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L52786) |
| `la_cgels` | subroutine | [`src/la_lapack_c.f90:53312`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L53312) |
| `la_cheev` | subroutine | [`src/la_lapack_c.f90:56623`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L56623) |
| `la_cheevr` | subroutine | [`src/la_lapack_c.f90:56781`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L56781) |
| `la_cheevx` | subroutine | [`src/la_lapack_c.f90:57074`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L57074) |
| `la_chesvx` | subroutine | [`src/la_lapack_c.f90:57973`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L57973) |
| `la_chgeqz` | subroutine | [`src/la_lapack_c.f90:58097`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L58097) |
| `la_chpev` | subroutine | [`src/la_lapack_c.f90:58645`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L58645) |
| `la_chpevx` | subroutine | [`src/la_lapack_c.f90:58744`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L58744) |
| `la_chpsvx` | subroutine | [`src/la_lapack_c.f90:59403`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L59403) |
| `la_chsein` | subroutine | [`src/la_lapack_c.f90:59481`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L59481) |
| `la_cpbsvx` | subroutine | [`src/la_lapack_c.f90:60589`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L60589) |
| `la_cposvx` | subroutine | [`src/la_lapack_c.f90:61130`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L61130) |
| `la_cgelsd` | subroutine | [`src/la_lapack_c.f90:63905`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L63905) |
| `la_cgelss` | subroutine | [`src/la_lapack_c.f90:64229`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L64229) |
| `la_cgelsy` | subroutine | [`src/la_lapack_c.f90:64706`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L64706) |
| `la_cgesdd` | subroutine | [`src/la_lapack_c.f90:65223`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L65223) |
| `la_cgesvd` | subroutine | [`src/la_lapack_c.f90:66759`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L66759) |
| `la_cgesvx` | subroutine | [`src/la_lapack_c.f90:70078`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L70078) |
| `la_cgetsls` | subroutine | [`src/la_lapack_c.f90:70295`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L70295) |
| `la_chbev` | subroutine | [`src/la_lapack_c.f90:71824`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L71824) |
| `la_chbevd` | subroutine | [`src/la_lapack_c.f90:71935`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L71935) |
| `la_chbevx` | subroutine | [`src/la_lapack_c.f90:72079`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L72079) |
| `la_cheevd` | subroutine | [`src/la_lapack_c.f90:72709`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L72709) |
| `la_chpevd` | subroutine | [`src/la_lapack_c.f90:72993`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L72993) |
| `la_cgeev` | subroutine | [`src/la_lapack_c.f90:73641`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L73641) |
| `la_cgeevx` | subroutine | [`src/la_lapack_c.f90:73905`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_c.f90#L73905) |
| `la_dla_gbrcond` | function | [`src/la_lapack_d.f90:27716`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L27716) |
| `la_dla_gercond` | function | [`src/la_lapack_d.f90:28053`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L28053) |
| `la_dla_porcond` | function | [`src/la_lapack_d.f90:28244`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L28244) |
| `la_dla_syrcond` | function | [`src/la_lapack_d.f90:28592`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L28592) |
| `la_dla_syrpvgrw` | function | [`src/la_lapack_d.f90:28756`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L28756) |
| `la_dlangb` | function | [`src/la_lapack_d.f90:29947`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L29947) |
| `la_dlanhs` | function | [`src/la_lapack_d.f90:30172`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L30172) |
| `la_dlansb` | function | [`src/la_lapack_d.f90:30244`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L30244) |
| `la_dlansf` | function | [`src/la_lapack_d.f90:30349`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L30349) |
| `la_dlansp` | function | [`src/la_lapack_d.f90:31053`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L31053) |
| `la_dlantb` | function | [`src/la_lapack_d.f90:31337`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L31337) |
| `la_dlantp` | function | [`src/la_lapack_d.f90:31530`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L31530) |
| `la_dlantr` | function | [`src/la_lapack_d.f90:31736`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L31736) |
| `la_dppsvx` | subroutine | [`src/la_lapack_d.f90:37892`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L37892) |
| `la_dspsvx` | subroutine | [`src/la_lapack_d.f90:39004`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L39004) |
| `la_dtbcon` | subroutine | [`src/la_lapack_d.f90:41597`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L41597) |
| `la_dtpcon` | subroutine | [`src/la_lapack_d.f90:42852`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L42852) |
| `la_dtrcon` | subroutine | [`src/la_lapack_d.f90:43377`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L43377) |
| `la_dgbsvx` | subroutine | [`src/la_lapack_d.f90:43646`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L43646) |
| `la_dhgeqz` | subroutine | [`src/la_lapack_d.f90:47629`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L47629) |
| `la_dsbev` | subroutine | [`src/la_lapack_d.f90:54777`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L54777) |
| `la_dsbevx` | subroutine | [`src/la_lapack_d.f90:54881`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L54881) |
| `la_dspev` | subroutine | [`src/la_lapack_d.f90:55545`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L55545) |
| `la_dspevx` | subroutine | [`src/la_lapack_d.f90:55640`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L55640) |
| `la_dgesvx` | subroutine | [`src/la_lapack_d.f90:63459`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L63459) |
| `la_dhsein` | subroutine | [`src/la_lapack_d.f90:65313`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L65313) |
| `la_dla_porpvgrw` | function | [`src/la_lapack_d.f90:65528`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L65528) |
| `la_dpbsvx` | subroutine | [`src/la_lapack_d.f90:67204`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L67204) |
| `la_dsbevd` | subroutine | [`src/la_lapack_d.f90:71874`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L71874) |
| `la_dspevd` | subroutine | [`src/la_lapack_d.f90:72123`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_d.f90#L72123) |
| `la_qgbsvx` | subroutine | [`src/la_lapack_q.f90:2866`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L2866) |
| `la_qgels` | subroutine | [`src/la_lapack_q.f90:7148`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L7148) |
| `la_qgelsd` | subroutine | [`src/la_lapack_q.f90:7372`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L7372) |
| `la_qgelss` | subroutine | [`src/la_lapack_q.f90:7682`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L7682) |
| `la_qgelsy` | subroutine | [`src/la_lapack_q.f90:8144`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L8144) |
| `la_qgesdd` | subroutine | [`src/la_lapack_q.f90:10097`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L10097) |
| `la_qgesvd` | subroutine | [`src/la_lapack_q.f90:11108`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L11108) |
| `la_qgesvx` | subroutine | [`src/la_lapack_q.f90:15205`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L15205) |
| `la_qgetsls` | subroutine | [`src/la_lapack_q.f90:15942`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L15942) |
| `la_qhgeqz` | subroutine | [`src/la_lapack_q.f90:21717`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L21717) |
| `la_qhsein` | subroutine | [`src/la_lapack_q.f90:22555`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L22555) |
| `la_qla_gbrcond` | function | [`src/la_lapack_q.f90:23121`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L23121) |
| `la_qla_gercond` | function | [`src/la_lapack_q.f90:23498`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L23498) |
| `la_qla_porcond` | function | [`src/la_lapack_q.f90:23728`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L23728) |
| `la_qla_porpvgrw` | function | [`src/la_lapack_q.f90:23884`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L23884) |
| `la_qla_syrcond` | function | [`src/la_lapack_q.f90:24164`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L24164) |
| `la_qla_syrpvgrw` | function | [`src/la_lapack_q.f90:24328`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L24328) |
| `la_qlaexc` | subroutine | [`src/la_lapack_q.f90:28043`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L28043) |
| `la_qlangb` | function | [`src/la_lapack_q.f90:31332`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L31332) |
| `la_qlange` | function | [`src/la_lapack_q.f90:31407`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L31407) |
| `la_qlanhs` | function | [`src/la_lapack_q.f90:31555`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L31555) |
| `la_qlansb` | function | [`src/la_lapack_q.f90:31627`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L31627) |
| `la_qlansf` | function | [`src/la_lapack_q.f90:31732`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L31732) |
| `la_qlansp` | function | [`src/la_lapack_q.f90:32436`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L32436) |
| `la_qlansy` | function | [`src/la_lapack_q.f90:32622`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L32622) |
| `la_qlantb` | function | [`src/la_lapack_q.f90:32718`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L32718) |
| `la_qlantp` | function | [`src/la_lapack_q.f90:32911`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L32911) |
| `la_qlantr` | function | [`src/la_lapack_q.f90:33117`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L33117) |
| `la_qlaqtr` | subroutine | [`src/la_lapack_q.f90:36278`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L36278) |
| `la_qpbsvx` | subroutine | [`src/la_lapack_q.f90:56867`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L56867) |
| `la_qposvx` | subroutine | [`src/la_lapack_q.f90:58250`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L58250) |
| `la_qppsvx` | subroutine | [`src/la_lapack_q.f90:59199`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L59199) |
| `la_qsbev` | subroutine | [`src/la_lapack_q.f90:60760`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L60760) |
| `la_qsbevd` | subroutine | [`src/la_lapack_q.f90:60869`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L60869) |
| `la_qsbevx` | subroutine | [`src/la_lapack_q.f90:60996`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L60996) |
| `la_qsgesv` | subroutine | [`src/la_lapack_q.f90:63125`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L63125) |
| `la_qspev` | subroutine | [`src/la_lapack_q.f90:63359`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L63359) |
| `la_qspevd` | subroutine | [`src/la_lapack_q.f90:63459`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L63459) |
| `la_qspevx` | subroutine | [`src/la_lapack_q.f90:63579`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L63579) |
| `la_qsposv` | subroutine | [`src/la_lapack_q.f90:64258`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L64258) |
| `la_qspsvx` | subroutine | [`src/la_lapack_q.f90:64652`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L64652) |
| `la_qsyev` | subroutine | [`src/la_lapack_q.f90:69089`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L69089) |
| `la_qsyevd` | subroutine | [`src/la_lapack_q.f90:69205`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L69205) |
| `la_qsyevr` | subroutine | [`src/la_lapack_q.f90:69378`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L69378) |
| `la_qsyevx` | subroutine | [`src/la_lapack_q.f90:69654`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L69654) |
| `la_qsysvx` | subroutine | [`src/la_lapack_q.f90:71005`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L71005) |
| `la_qtbcon` | subroutine | [`src/la_lapack_q.f90:74913`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L74913) |
| `la_qtpcon` | subroutine | [`src/la_lapack_q.f90:79618`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L79618) |
| `la_qtrcon` | subroutine | [`src/la_lapack_q.f90:81388`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L81388) |
| `la_qtrsyl` | subroutine | [`src/la_lapack_q.f90:83806`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_q.f90#L83806) |
| `la_sla_gbrcond` | function | [`src/la_lapack_s.f90:27629`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L27629) |
| `la_sla_gercond` | function | [`src/la_lapack_s.f90:27966`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L27966) |
| `la_sla_porcond` | function | [`src/la_lapack_s.f90:28157`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L28157) |
| `la_sla_syrcond` | function | [`src/la_lapack_s.f90:28505`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L28505) |
| `la_sla_syrpvgrw` | function | [`src/la_lapack_s.f90:28669`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L28669) |
| `la_slangb` | function | [`src/la_lapack_s.f90:29860`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L29860) |
| `la_slange` | function | [`src/la_lapack_s.f90:29935`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L29935) |
| `la_slanhs` | function | [`src/la_lapack_s.f90:30083`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L30083) |
| `la_slansb` | function | [`src/la_lapack_s.f90:30155`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L30155) |
| `la_slansf` | function | [`src/la_lapack_s.f90:30260`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L30260) |
| `la_slansp` | function | [`src/la_lapack_s.f90:30964`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L30964) |
| `la_slansy` | function | [`src/la_lapack_s.f90:31150`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L31150) |
| `la_slantb` | function | [`src/la_lapack_s.f90:31246`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L31246) |
| `la_slantp` | function | [`src/la_lapack_s.f90:31439`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L31439) |
| `la_slantr` | function | [`src/la_lapack_s.f90:31645`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L31645) |
| `la_sppsvx` | subroutine | [`src/la_lapack_s.f90:37802`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L37802) |
| `la_sspsvx` | subroutine | [`src/la_lapack_s.f90:38914`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L38914) |
| `la_stbcon` | subroutine | [`src/la_lapack_s.f90:41506`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L41506) |
| `la_stpcon` | subroutine | [`src/la_lapack_s.f90:42761`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L42761) |
| `la_strcon` | subroutine | [`src/la_lapack_s.f90:43286`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L43286) |
| `la_sgbsvx` | subroutine | [`src/la_lapack_s.f90:43555`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L43555) |
| `la_shgeqz` | subroutine | [`src/la_lapack_s.f90:46462`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L46462) |
| `la_slaqtr` | subroutine | [`src/la_lapack_s.f90:50683`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L50683) |
| `la_ssbev` | subroutine | [`src/la_lapack_s.f90:53610`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L53610) |
| `la_ssbevx` | subroutine | [`src/la_lapack_s.f90:53714`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L53714) |
| `la_sspev` | subroutine | [`src/la_lapack_s.f90:54201`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54201) |
| `la_sspevx` | subroutine | [`src/la_lapack_s.f90:54296`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54296) |
| `la_ssyev` | subroutine | [`src/la_lapack_s.f90:54703`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54703) |
| `la_ssyevx` | subroutine | [`src/la_lapack_s.f90:54812`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L54812) |
| `la_ssysvx` | subroutine | [`src/la_lapack_s.f90:55367`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L55367) |
| `la_strsyl` | subroutine | [`src/la_lapack_s.f90:59355`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L59355) |
| `la_sgels` | subroutine | [`src/la_lapack_s.f90:60307`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L60307) |
| `la_sgesvx` | subroutine | [`src/la_lapack_s.f90:60960`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L60960) |
| `la_shsein` | subroutine | [`src/la_lapack_s.f90:62813`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L62813) |
| `la_sla_porpvgrw` | function | [`src/la_lapack_s.f90:63028`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L63028) |
| `la_slaexc` | subroutine | [`src/la_lapack_s.f90:63386`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L63386) |
| `la_spbsvx` | subroutine | [`src/la_lapack_s.f90:64703`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L64703) |
| `la_sposvx` | subroutine | [`src/la_lapack_s.f90:65085`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L65085) |
| `la_sgelsy` | subroutine | [`src/la_lapack_s.f90:66022`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L66022) |
| `la_sgetsls` | subroutine | [`src/la_lapack_s.f90:66355`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L66355) |
| `la_ssyevd` | subroutine | [`src/la_lapack_s.f90:68030`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L68030) |
| `la_ssbevd` | subroutine | [`src/la_lapack_s.f90:68283`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L68283) |
| `la_sspevd` | subroutine | [`src/la_lapack_s.f90:68532`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L68532) |
| `la_sgelsd` | subroutine | [`src/la_lapack_s.f90:71715`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L71715) |
| `la_sgelss` | subroutine | [`src/la_lapack_s.f90:72028`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L72028) |
| `la_sgesdd` | subroutine | [`src/la_lapack_s.f90:72474`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L72474) |
| `la_sgesvd` | subroutine | [`src/la_lapack_s.f90:73437`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L73437) |
| `la_ssyevr` | subroutine | [`src/la_lapack_s.f90:84140`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_s.f90#L84140) |
| `la_wcgesv` | subroutine | [`src/la_lapack_w.f90:1628`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L1628) |
| `la_wcposv` | subroutine | [`src/la_lapack_w.f90:1812`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L1812) |
| `la_wgbsvx` | subroutine | [`src/la_lapack_w.f90:2977`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L2977) |
| `la_wgeev` | subroutine | [`src/la_lapack_w.f90:4877`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L4877) |
| `la_wgeevx` | subroutine | [`src/la_lapack_w.f90:5141`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L5141) |
| `la_wgels` | subroutine | [`src/la_lapack_w.f90:7440`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L7440) |
| `la_wgelsd` | subroutine | [`src/la_lapack_w.f90:7664`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L7664) |
| `la_wgelss` | subroutine | [`src/la_lapack_w.f90:7988`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L7988) |
| `la_wgelsy` | subroutine | [`src/la_lapack_w.f90:8465`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L8465) |
| `la_wgesdd` | subroutine | [`src/la_lapack_w.f90:10419`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L10419) |
| `la_wgesvd` | subroutine | [`src/la_lapack_w.f90:11955`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L11955) |
| `la_wgesvx` | subroutine | [`src/la_lapack_w.f90:16122`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L16122) |
| `la_wgetsls` | subroutine | [`src/la_lapack_w.f90:16861`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L16861) |
| `la_whbev` | subroutine | [`src/la_lapack_w.f90:22271`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L22271) |
| `la_whbevd` | subroutine | [`src/la_lapack_w.f90:22382`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L22382) |
| `la_whbevx` | subroutine | [`src/la_lapack_w.f90:22526`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L22526) |
| `la_wheev` | subroutine | [`src/la_lapack_w.f90:24786`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L24786) |
| `la_wheevd` | subroutine | [`src/la_lapack_w.f90:24903`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L24903) |
| `la_wheevr` | subroutine | [`src/la_lapack_w.f90:25096`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L25096) |
| `la_wheevx` | subroutine | [`src/la_lapack_w.f90:25389`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L25389) |
| `la_whesvx` | subroutine | [`src/la_lapack_w.f90:26763`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L26763) |
| `la_whgeqz` | subroutine | [`src/la_lapack_w.f90:31301`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L31301) |
| `la_whpev` | subroutine | [`src/la_lapack_w.f90:31849`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L31849) |
| `la_whpevd` | subroutine | [`src/la_lapack_w.f90:31953`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L31953) |
| `la_whpevx` | subroutine | [`src/la_lapack_w.f90:32089`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L32089) |
| `la_whpsvx` | subroutine | [`src/la_lapack_w.f90:33009`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L33009) |
| `la_whsein` | subroutine | [`src/la_lapack_w.f90:33999`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L33999) |
| `la_wla_gbrcond_c` | function | [`src/la_lapack_w.f90:34506`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L34506) |
| `la_wla_gercond_c` | function | [`src/la_lapack_w.f90:34888`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L34888) |
| `la_wla_hercond_c` | function | [`src/la_lapack_w.f90:35267`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L35267) |
| `la_wla_herpvgrw` | function | [`src/la_lapack_w.f90:35421`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L35421) |
| `la_wla_porcond_c` | function | [`src/la_lapack_w.f90:35652`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L35652) |
| `la_wla_porpvgrw` | function | [`src/la_lapack_w.f90:35806`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L35806) |
| `la_wla_syrcond_c` | function | [`src/la_lapack_w.f90:36090`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L36090) |
| `la_wla_syrpvgrw` | function | [`src/la_lapack_w.f90:36245`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L36245) |
| `la_wlangb` | function | [`src/la_lapack_w.f90:42180`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L42180) |
| `la_wlange` | function | [`src/la_lapack_w.f90:42255`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L42255) |
| `la_wlanhb` | function | [`src/la_lapack_w.f90:42403`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L42403) |
| `la_wlanhe` | function | [`src/la_lapack_w.f90:42522`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L42522) |
| `la_wlanhf` | function | [`src/la_lapack_w.f90:42632`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L42632) |
| `la_wlanhp` | function | [`src/la_lapack_w.f90:43852`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L43852) |
| `la_wlanhs` | function | [`src/la_lapack_w.f90:43980`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L43980) |
| `la_wlansb` | function | [`src/la_lapack_w.f90:44115`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44115) |
| `la_wlansp` | function | [`src/la_lapack_w.f90:44220`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44220) |
| `la_wlansy` | function | [`src/la_lapack_w.f90:44353`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44353) |
| `la_wlantb` | function | [`src/la_lapack_w.f90:44449`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44449) |
| `la_wlantp` | function | [`src/la_lapack_w.f90:44642`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44642) |
| `la_wlantr` | function | [`src/la_lapack_w.f90:44848`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L44848) |
| `la_wpbsvx` | subroutine | [`src/la_lapack_w.f90:56719`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L56719) |
| `la_wposvx` | subroutine | [`src/la_lapack_w.f90:58120`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L58120) |
| `la_wppsvx` | subroutine | [`src/la_lapack_w.f90:59087`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L59087) |
| `la_wspsvx` | subroutine | [`src/la_lapack_w.f90:61273`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L61273) |
| `la_wsysvx` | subroutine | [`src/la_lapack_w.f90:65137`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L65137) |
| `la_wtbcon` | subroutine | [`src/la_lapack_w.f90:68407`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L68407) |
| `la_wtpcon` | subroutine | [`src/la_lapack_w.f90:71879`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L71879) |
| `la_wtrcon` | subroutine | [`src/la_lapack_w.f90:73697`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L73697) |
| `la_wtrsyl` | subroutine | [`src/la_lapack_w.f90:74903`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_w.f90#L74903) |
| `la_zla_porpvgrw` | function | [`src/la_lapack_z.f90:6143`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L6143) |
| `la_zla_gbrcond_c` | function | [`src/la_lapack_z.f90:38535`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L38535) |
| `la_zla_gercond_c` | function | [`src/la_lapack_z.f90:38683`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L38683) |
| `la_zla_hercond_c` | function | [`src/la_lapack_z.f90:38824`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L38824) |
| `la_zla_herpvgrw` | function | [`src/la_lapack_z.f90:38978`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L38978) |
| `la_zla_porcond_c` | function | [`src/la_lapack_z.f90:39163`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L39163) |
| `la_zla_syrcond_c` | function | [`src/la_lapack_z.f90:39313`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L39313) |
| `la_zla_syrpvgrw` | function | [`src/la_lapack_z.f90:39468`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L39468) |
| `la_zlangb` | function | [`src/la_lapack_z.f90:41592`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L41592) |
| `la_zlanhb` | function | [`src/la_lapack_z.f90:41817`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L41817) |
| `la_zlanhe` | function | [`src/la_lapack_z.f90:41936`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L41936) |
| `la_zlanhf` | function | [`src/la_lapack_z.f90:42046`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L42046) |
| `la_zlanhp` | function | [`src/la_lapack_z.f90:43266`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43266) |
| `la_zlanhs` | function | [`src/la_lapack_z.f90:43394`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43394) |
| `la_zlansb` | function | [`src/la_lapack_z.f90:43529`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43529) |
| `la_zlansp` | function | [`src/la_lapack_z.f90:43634`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43634) |
| `la_zlansy` | function | [`src/la_lapack_z.f90:43767`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43767) |
| `la_zlantb` | function | [`src/la_lapack_z.f90:43863`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L43863) |
| `la_zlantp` | function | [`src/la_lapack_z.f90:44056`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L44056) |
| `la_zlantr` | function | [`src/la_lapack_z.f90:44262`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L44262) |
| `la_zppsvx` | subroutine | [`src/la_lapack_z.f90:47423`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L47423) |
| `la_zspsvx` | subroutine | [`src/la_lapack_z.f90:48113`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L48113) |
| `la_zsysvx` | subroutine | [`src/la_lapack_z.f90:49210`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L49210) |
| `la_ztbcon` | subroutine | [`src/la_lapack_z.f90:49307`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L49307) |
| `la_ztpcon` | subroutine | [`src/la_lapack_z.f90:50384`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L50384) |
| `la_ztrcon` | subroutine | [`src/la_lapack_z.f90:50850`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L50850) |
| `la_zcposv` | subroutine | [`src/la_lapack_z.f90:52380`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L52380) |
| `la_zgbsvx` | subroutine | [`src/la_lapack_z.f90:53072`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L53072) |
| `la_zheev` | subroutine | [`src/la_lapack_z.f90:56909`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L56909) |
| `la_zheevr` | subroutine | [`src/la_lapack_z.f90:57067`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L57067) |
| `la_zheevx` | subroutine | [`src/la_lapack_z.f90:57360`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L57360) |
| `la_zhesvx` | subroutine | [`src/la_lapack_z.f90:58260`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L58260) |
| `la_zhgeqz` | subroutine | [`src/la_lapack_z.f90:58384`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L58384) |
| `la_zhpev` | subroutine | [`src/la_lapack_z.f90:58932`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L58932) |
| `la_zhpevx` | subroutine | [`src/la_lapack_z.f90:59031`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L59031) |
| `la_zhpsvx` | subroutine | [`src/la_lapack_z.f90:59690`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L59690) |
| `la_zhsein` | subroutine | [`src/la_lapack_z.f90:59768`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L59768) |
| `la_zpbsvx` | subroutine | [`src/la_lapack_z.f90:60876`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L60876) |
| `la_zposvx` | subroutine | [`src/la_lapack_z.f90:61417`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L61417) |
| `la_zgesvx` | subroutine | [`src/la_lapack_z.f90:70546`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L70546) |
| `la_zhbev` | subroutine | [`src/la_lapack_z.f90:72292`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L72292) |
| `la_zhbevd` | subroutine | [`src/la_lapack_z.f90:72403`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L72403) |
| `la_zhbevx` | subroutine | [`src/la_lapack_z.f90:72547`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L72547) |
| `la_zheevd` | subroutine | [`src/la_lapack_z.f90:73177`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L73177) |
| `la_zhpevd` | subroutine | [`src/la_lapack_z.f90:73461`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack_z.f90#L73461) |
| `la_slstsq_one` | function | [`src/la_least_squares.f90:249`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L249) |
| `la_dlstsq_one` | function | [`src/la_least_squares.f90:355`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L355) |
| `la_qlstsq_one` | function | [`src/la_least_squares.f90:461`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L461) |
| `la_clstsq_one` | function | [`src/la_least_squares.f90:567`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L567) |
| `la_zlstsq_one` | function | [`src/la_least_squares.f90:673`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L673) |
| `la_wlstsq_one` | function | [`src/la_least_squares.f90:779`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L779) |
| `la_slstsq_multiple` | function | [`src/la_least_squares.f90:885`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L885) |
| `la_dlstsq_multiple` | function | [`src/la_least_squares.f90:991`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L991) |
| `la_qlstsq_multiple` | function | [`src/la_least_squares.f90:1097`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L1097) |
| `la_clstsq_multiple` | function | [`src/la_least_squares.f90:1203`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L1203) |
| `la_zlstsq_multiple` | function | [`src/la_least_squares.f90:1309`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L1309) |
| `la_wlstsq_multiple` | function | [`src/la_least_squares.f90:1415`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_least_squares.f90#L1415) |
| `la_norm_1d_order_err_char_s` | function | [`src/la_norms.f90:748`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L748) |
| `la_norm_2d_order_err_char_s` | function | [`src/la_norms.f90:831`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L831) |
| `la_norm_3d_order_err_char_s` | function | [`src/la_norms.f90:914`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L914) |
| `la_norm_4d_order_err_char_s` | function | [`src/la_norms.f90:997`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L997) |
| `la_norm_5d_order_err_char_s` | function | [`src/la_norms.f90:1080`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1080) |
| `la_norm_6d_order_err_char_s` | function | [`src/la_norms.f90:1163`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1163) |
| `la_norm_7d_order_err_char_s` | function | [`src/la_norms.f90:1246`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1246) |
| `la_norm_2d_to_1d_err_char_s` | function | [`src/la_norms.f90:1335`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1335) |
| `la_norm_3d_to_2d_err_char_s` | function | [`src/la_norms.f90:1431`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1431) |
| `la_norm_4d_to_3d_err_char_s` | function | [`src/la_norms.f90:1528`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1528) |
| `la_norm_5d_to_4d_err_char_s` | function | [`src/la_norms.f90:1627`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1627) |
| `la_norm_6d_to_5d_err_char_s` | function | [`src/la_norms.f90:1726`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1726) |
| `la_norm_7d_to_6d_err_char_s` | function | [`src/la_norms.f90:1827`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1827) |
| `matrix_norm_char_s` | function | [`src/la_norms.f90:1916`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1916) |
| `matrix_norm_3d_to_1d_char_s` | function | [`src/la_norms.f90:1966`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L1966) |
| `matrix_norm_4d_to_2d_char_s` | function | [`src/la_norms.f90:2065`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2065) |
| `matrix_norm_5d_to_3d_char_s` | function | [`src/la_norms.f90:2165`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2165) |
| `matrix_norm_6d_to_4d_char_s` | function | [`src/la_norms.f90:2266`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2266) |
| `matrix_norm_7d_to_5d_char_s` | function | [`src/la_norms.f90:2368`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2368) |
| `la_norm_1d_order_err_int_s` | function | [`src/la_norms.f90:2488`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2488) |
| `la_norm_2d_order_err_int_s` | function | [`src/la_norms.f90:2571`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2571) |
| `la_norm_3d_order_err_int_s` | function | [`src/la_norms.f90:2654`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2654) |
| `la_norm_4d_order_err_int_s` | function | [`src/la_norms.f90:2737`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2737) |
| `la_norm_5d_order_err_int_s` | function | [`src/la_norms.f90:2820`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2820) |
| `la_norm_6d_order_err_int_s` | function | [`src/la_norms.f90:2903`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2903) |
| `la_norm_7d_order_err_int_s` | function | [`src/la_norms.f90:2986`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L2986) |
| `la_norm_2d_to_1d_err_int_s` | function | [`src/la_norms.f90:3075`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3075) |
| `la_norm_3d_to_2d_err_int_s` | function | [`src/la_norms.f90:3171`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3171) |
| `la_norm_4d_to_3d_err_int_s` | function | [`src/la_norms.f90:3268`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3268) |
| `la_norm_5d_to_4d_err_int_s` | function | [`src/la_norms.f90:3367`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3367) |
| `la_norm_6d_to_5d_err_int_s` | function | [`src/la_norms.f90:3466`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3466) |
| `la_norm_7d_to_6d_err_int_s` | function | [`src/la_norms.f90:3567`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3567) |
| `matrix_norm_int_s` | function | [`src/la_norms.f90:3656`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3656) |
| `matrix_norm_3d_to_1d_int_s` | function | [`src/la_norms.f90:3706`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3706) |
| `matrix_norm_4d_to_2d_int_s` | function | [`src/la_norms.f90:3805`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3805) |
| `matrix_norm_5d_to_3d_int_s` | function | [`src/la_norms.f90:3905`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L3905) |
| `matrix_norm_6d_to_4d_int_s` | function | [`src/la_norms.f90:4006`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4006) |
| `matrix_norm_7d_to_5d_int_s` | function | [`src/la_norms.f90:4108`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4108) |
| `la_norm_1d_order_err_char_d` | function | [`src/la_norms.f90:4228`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4228) |
| `la_norm_2d_order_err_char_d` | function | [`src/la_norms.f90:4311`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4311) |
| `la_norm_3d_order_err_char_d` | function | [`src/la_norms.f90:4394`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4394) |
| `la_norm_4d_order_err_char_d` | function | [`src/la_norms.f90:4477`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4477) |
| `la_norm_5d_order_err_char_d` | function | [`src/la_norms.f90:4560`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4560) |
| `la_norm_6d_order_err_char_d` | function | [`src/la_norms.f90:4643`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4643) |
| `la_norm_7d_order_err_char_d` | function | [`src/la_norms.f90:4726`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4726) |
| `la_norm_2d_to_1d_err_char_d` | function | [`src/la_norms.f90:4815`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4815) |
| `la_norm_3d_to_2d_err_char_d` | function | [`src/la_norms.f90:4911`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L4911) |
| `la_norm_4d_to_3d_err_char_d` | function | [`src/la_norms.f90:5008`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5008) |
| `la_norm_5d_to_4d_err_char_d` | function | [`src/la_norms.f90:5107`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5107) |
| `la_norm_6d_to_5d_err_char_d` | function | [`src/la_norms.f90:5206`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5206) |
| `la_norm_7d_to_6d_err_char_d` | function | [`src/la_norms.f90:5307`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5307) |
| `matrix_norm_char_d` | function | [`src/la_norms.f90:5396`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5396) |
| `matrix_norm_3d_to_1d_char_d` | function | [`src/la_norms.f90:5446`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5446) |
| `matrix_norm_4d_to_2d_char_d` | function | [`src/la_norms.f90:5545`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5545) |
| `matrix_norm_5d_to_3d_char_d` | function | [`src/la_norms.f90:5645`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5645) |
| `matrix_norm_6d_to_4d_char_d` | function | [`src/la_norms.f90:5746`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5746) |
| `matrix_norm_7d_to_5d_char_d` | function | [`src/la_norms.f90:5848`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5848) |
| `la_norm_1d_order_err_int_d` | function | [`src/la_norms.f90:5968`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L5968) |
| `la_norm_2d_order_err_int_d` | function | [`src/la_norms.f90:6051`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6051) |
| `la_norm_3d_order_err_int_d` | function | [`src/la_norms.f90:6134`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6134) |
| `la_norm_4d_order_err_int_d` | function | [`src/la_norms.f90:6217`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6217) |
| `la_norm_5d_order_err_int_d` | function | [`src/la_norms.f90:6300`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6300) |
| `la_norm_6d_order_err_int_d` | function | [`src/la_norms.f90:6383`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6383) |
| `la_norm_7d_order_err_int_d` | function | [`src/la_norms.f90:6466`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6466) |
| `la_norm_2d_to_1d_err_int_d` | function | [`src/la_norms.f90:6555`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6555) |
| `la_norm_3d_to_2d_err_int_d` | function | [`src/la_norms.f90:6651`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6651) |
| `la_norm_4d_to_3d_err_int_d` | function | [`src/la_norms.f90:6748`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6748) |
| `la_norm_5d_to_4d_err_int_d` | function | [`src/la_norms.f90:6847`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6847) |
| `la_norm_6d_to_5d_err_int_d` | function | [`src/la_norms.f90:6946`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L6946) |
| `la_norm_7d_to_6d_err_int_d` | function | [`src/la_norms.f90:7047`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7047) |
| `matrix_norm_int_d` | function | [`src/la_norms.f90:7136`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7136) |
| `matrix_norm_3d_to_1d_int_d` | function | [`src/la_norms.f90:7186`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7186) |
| `matrix_norm_4d_to_2d_int_d` | function | [`src/la_norms.f90:7285`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7285) |
| `matrix_norm_5d_to_3d_int_d` | function | [`src/la_norms.f90:7385`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7385) |
| `matrix_norm_6d_to_4d_int_d` | function | [`src/la_norms.f90:7486`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7486) |
| `matrix_norm_7d_to_5d_int_d` | function | [`src/la_norms.f90:7588`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7588) |
| `la_norm_1d_order_err_char_q` | function | [`src/la_norms.f90:7708`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7708) |
| `la_norm_2d_order_err_char_q` | function | [`src/la_norms.f90:7791`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7791) |
| `la_norm_3d_order_err_char_q` | function | [`src/la_norms.f90:7874`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7874) |
| `la_norm_4d_order_err_char_q` | function | [`src/la_norms.f90:7957`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L7957) |
| `la_norm_5d_order_err_char_q` | function | [`src/la_norms.f90:8040`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8040) |
| `la_norm_6d_order_err_char_q` | function | [`src/la_norms.f90:8123`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8123) |
| `la_norm_7d_order_err_char_q` | function | [`src/la_norms.f90:8206`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8206) |
| `la_norm_2d_to_1d_err_char_q` | function | [`src/la_norms.f90:8295`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8295) |
| `la_norm_3d_to_2d_err_char_q` | function | [`src/la_norms.f90:8391`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8391) |
| `la_norm_4d_to_3d_err_char_q` | function | [`src/la_norms.f90:8488`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8488) |
| `la_norm_5d_to_4d_err_char_q` | function | [`src/la_norms.f90:8587`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8587) |
| `la_norm_6d_to_5d_err_char_q` | function | [`src/la_norms.f90:8686`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8686) |
| `la_norm_7d_to_6d_err_char_q` | function | [`src/la_norms.f90:8787`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8787) |
| `matrix_norm_char_q` | function | [`src/la_norms.f90:8876`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8876) |
| `matrix_norm_3d_to_1d_char_q` | function | [`src/la_norms.f90:8926`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L8926) |
| `matrix_norm_4d_to_2d_char_q` | function | [`src/la_norms.f90:9025`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9025) |
| `matrix_norm_5d_to_3d_char_q` | function | [`src/la_norms.f90:9125`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9125) |
| `matrix_norm_6d_to_4d_char_q` | function | [`src/la_norms.f90:9226`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9226) |
| `matrix_norm_7d_to_5d_char_q` | function | [`src/la_norms.f90:9328`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9328) |
| `la_norm_1d_order_err_int_q` | function | [`src/la_norms.f90:9448`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9448) |
| `la_norm_2d_order_err_int_q` | function | [`src/la_norms.f90:9531`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9531) |
| `la_norm_3d_order_err_int_q` | function | [`src/la_norms.f90:9614`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9614) |
| `la_norm_4d_order_err_int_q` | function | [`src/la_norms.f90:9697`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9697) |
| `la_norm_5d_order_err_int_q` | function | [`src/la_norms.f90:9780`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9780) |
| `la_norm_6d_order_err_int_q` | function | [`src/la_norms.f90:9863`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9863) |
| `la_norm_7d_order_err_int_q` | function | [`src/la_norms.f90:9946`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L9946) |
| `la_norm_2d_to_1d_err_int_q` | function | [`src/la_norms.f90:10035`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10035) |
| `la_norm_3d_to_2d_err_int_q` | function | [`src/la_norms.f90:10131`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10131) |
| `la_norm_4d_to_3d_err_int_q` | function | [`src/la_norms.f90:10228`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10228) |
| `la_norm_5d_to_4d_err_int_q` | function | [`src/la_norms.f90:10327`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10327) |
| `la_norm_6d_to_5d_err_int_q` | function | [`src/la_norms.f90:10426`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10426) |
| `la_norm_7d_to_6d_err_int_q` | function | [`src/la_norms.f90:10527`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10527) |
| `matrix_norm_int_q` | function | [`src/la_norms.f90:10616`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10616) |
| `matrix_norm_3d_to_1d_int_q` | function | [`src/la_norms.f90:10666`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10666) |
| `matrix_norm_4d_to_2d_int_q` | function | [`src/la_norms.f90:10765`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10765) |
| `matrix_norm_5d_to_3d_int_q` | function | [`src/la_norms.f90:10865`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10865) |
| `matrix_norm_6d_to_4d_int_q` | function | [`src/la_norms.f90:10966`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L10966) |
| `matrix_norm_7d_to_5d_int_q` | function | [`src/la_norms.f90:11068`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11068) |
| `la_norm_1d_order_err_char_c` | function | [`src/la_norms.f90:11188`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11188) |
| `la_norm_2d_order_err_char_c` | function | [`src/la_norms.f90:11271`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11271) |
| `la_norm_3d_order_err_char_c` | function | [`src/la_norms.f90:11354`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11354) |
| `la_norm_4d_order_err_char_c` | function | [`src/la_norms.f90:11437`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11437) |
| `la_norm_5d_order_err_char_c` | function | [`src/la_norms.f90:11520`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11520) |
| `la_norm_6d_order_err_char_c` | function | [`src/la_norms.f90:11603`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11603) |
| `la_norm_7d_order_err_char_c` | function | [`src/la_norms.f90:11686`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11686) |
| `la_norm_2d_to_1d_err_char_c` | function | [`src/la_norms.f90:11775`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11775) |
| `la_norm_3d_to_2d_err_char_c` | function | [`src/la_norms.f90:11871`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11871) |
| `la_norm_4d_to_3d_err_char_c` | function | [`src/la_norms.f90:11968`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L11968) |
| `la_norm_5d_to_4d_err_char_c` | function | [`src/la_norms.f90:12067`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12067) |
| `la_norm_6d_to_5d_err_char_c` | function | [`src/la_norms.f90:12166`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12166) |
| `la_norm_7d_to_6d_err_char_c` | function | [`src/la_norms.f90:12267`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12267) |
| `matrix_norm_char_c` | function | [`src/la_norms.f90:12356`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12356) |
| `matrix_norm_3d_to_1d_char_c` | function | [`src/la_norms.f90:12406`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12406) |
| `matrix_norm_4d_to_2d_char_c` | function | [`src/la_norms.f90:12505`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12505) |
| `matrix_norm_5d_to_3d_char_c` | function | [`src/la_norms.f90:12605`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12605) |
| `matrix_norm_6d_to_4d_char_c` | function | [`src/la_norms.f90:12706`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12706) |
| `matrix_norm_7d_to_5d_char_c` | function | [`src/la_norms.f90:12808`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12808) |
| `la_norm_1d_order_err_int_c` | function | [`src/la_norms.f90:12928`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L12928) |
| `la_norm_2d_order_err_int_c` | function | [`src/la_norms.f90:13011`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13011) |
| `la_norm_3d_order_err_int_c` | function | [`src/la_norms.f90:13094`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13094) |
| `la_norm_4d_order_err_int_c` | function | [`src/la_norms.f90:13177`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13177) |
| `la_norm_5d_order_err_int_c` | function | [`src/la_norms.f90:13260`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13260) |
| `la_norm_6d_order_err_int_c` | function | [`src/la_norms.f90:13343`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13343) |
| `la_norm_7d_order_err_int_c` | function | [`src/la_norms.f90:13426`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13426) |
| `la_norm_2d_to_1d_err_int_c` | function | [`src/la_norms.f90:13515`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13515) |
| `la_norm_3d_to_2d_err_int_c` | function | [`src/la_norms.f90:13611`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13611) |
| `la_norm_4d_to_3d_err_int_c` | function | [`src/la_norms.f90:13708`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13708) |
| `la_norm_5d_to_4d_err_int_c` | function | [`src/la_norms.f90:13807`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13807) |
| `la_norm_6d_to_5d_err_int_c` | function | [`src/la_norms.f90:13906`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L13906) |
| `la_norm_7d_to_6d_err_int_c` | function | [`src/la_norms.f90:14007`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14007) |
| `matrix_norm_int_c` | function | [`src/la_norms.f90:14096`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14096) |
| `matrix_norm_3d_to_1d_int_c` | function | [`src/la_norms.f90:14146`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14146) |
| `matrix_norm_4d_to_2d_int_c` | function | [`src/la_norms.f90:14245`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14245) |
| `matrix_norm_5d_to_3d_int_c` | function | [`src/la_norms.f90:14345`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14345) |
| `matrix_norm_6d_to_4d_int_c` | function | [`src/la_norms.f90:14446`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14446) |
| `matrix_norm_7d_to_5d_int_c` | function | [`src/la_norms.f90:14548`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14548) |
| `la_norm_1d_order_err_char_z` | function | [`src/la_norms.f90:14668`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14668) |
| `la_norm_2d_order_err_char_z` | function | [`src/la_norms.f90:14751`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14751) |
| `la_norm_3d_order_err_char_z` | function | [`src/la_norms.f90:14834`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14834) |
| `la_norm_4d_order_err_char_z` | function | [`src/la_norms.f90:14917`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L14917) |
| `la_norm_5d_order_err_char_z` | function | [`src/la_norms.f90:15000`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15000) |
| `la_norm_6d_order_err_char_z` | function | [`src/la_norms.f90:15083`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15083) |
| `la_norm_7d_order_err_char_z` | function | [`src/la_norms.f90:15166`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15166) |
| `la_norm_2d_to_1d_err_char_z` | function | [`src/la_norms.f90:15255`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15255) |
| `la_norm_3d_to_2d_err_char_z` | function | [`src/la_norms.f90:15351`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15351) |
| `la_norm_4d_to_3d_err_char_z` | function | [`src/la_norms.f90:15448`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15448) |
| `la_norm_5d_to_4d_err_char_z` | function | [`src/la_norms.f90:15547`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15547) |
| `la_norm_6d_to_5d_err_char_z` | function | [`src/la_norms.f90:15646`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15646) |
| `la_norm_7d_to_6d_err_char_z` | function | [`src/la_norms.f90:15747`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15747) |
| `matrix_norm_char_z` | function | [`src/la_norms.f90:15836`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15836) |
| `matrix_norm_3d_to_1d_char_z` | function | [`src/la_norms.f90:15886`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15886) |
| `matrix_norm_4d_to_2d_char_z` | function | [`src/la_norms.f90:15985`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L15985) |
| `matrix_norm_5d_to_3d_char_z` | function | [`src/la_norms.f90:16085`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16085) |
| `matrix_norm_6d_to_4d_char_z` | function | [`src/la_norms.f90:16186`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16186) |
| `matrix_norm_7d_to_5d_char_z` | function | [`src/la_norms.f90:16288`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16288) |
| `la_norm_1d_order_err_int_z` | function | [`src/la_norms.f90:16408`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16408) |
| `la_norm_2d_order_err_int_z` | function | [`src/la_norms.f90:16491`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16491) |
| `la_norm_3d_order_err_int_z` | function | [`src/la_norms.f90:16574`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16574) |
| `la_norm_4d_order_err_int_z` | function | [`src/la_norms.f90:16657`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16657) |
| `la_norm_5d_order_err_int_z` | function | [`src/la_norms.f90:16740`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16740) |
| `la_norm_6d_order_err_int_z` | function | [`src/la_norms.f90:16823`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16823) |
| `la_norm_7d_order_err_int_z` | function | [`src/la_norms.f90:16906`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16906) |
| `la_norm_2d_to_1d_err_int_z` | function | [`src/la_norms.f90:16995`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L16995) |
| `la_norm_3d_to_2d_err_int_z` | function | [`src/la_norms.f90:17091`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17091) |
| `la_norm_4d_to_3d_err_int_z` | function | [`src/la_norms.f90:17188`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17188) |
| `la_norm_5d_to_4d_err_int_z` | function | [`src/la_norms.f90:17287`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17287) |
| `la_norm_6d_to_5d_err_int_z` | function | [`src/la_norms.f90:17386`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17386) |
| `la_norm_7d_to_6d_err_int_z` | function | [`src/la_norms.f90:17487`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17487) |
| `matrix_norm_int_z` | function | [`src/la_norms.f90:17576`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17576) |
| `matrix_norm_3d_to_1d_int_z` | function | [`src/la_norms.f90:17626`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17626) |
| `matrix_norm_4d_to_2d_int_z` | function | [`src/la_norms.f90:17725`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17725) |
| `matrix_norm_5d_to_3d_int_z` | function | [`src/la_norms.f90:17825`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17825) |
| `matrix_norm_6d_to_4d_int_z` | function | [`src/la_norms.f90:17926`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L17926) |
| `matrix_norm_7d_to_5d_int_z` | function | [`src/la_norms.f90:18028`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18028) |
| `la_norm_1d_order_err_char_w` | function | [`src/la_norms.f90:18148`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18148) |
| `la_norm_2d_order_err_char_w` | function | [`src/la_norms.f90:18231`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18231) |
| `la_norm_3d_order_err_char_w` | function | [`src/la_norms.f90:18314`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18314) |
| `la_norm_4d_order_err_char_w` | function | [`src/la_norms.f90:18397`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18397) |
| `la_norm_5d_order_err_char_w` | function | [`src/la_norms.f90:18480`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18480) |
| `la_norm_6d_order_err_char_w` | function | [`src/la_norms.f90:18563`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18563) |
| `la_norm_7d_order_err_char_w` | function | [`src/la_norms.f90:18646`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18646) |
| `la_norm_2d_to_1d_err_char_w` | function | [`src/la_norms.f90:18735`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18735) |
| `la_norm_3d_to_2d_err_char_w` | function | [`src/la_norms.f90:18831`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18831) |
| `la_norm_4d_to_3d_err_char_w` | function | [`src/la_norms.f90:18928`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L18928) |
| `la_norm_5d_to_4d_err_char_w` | function | [`src/la_norms.f90:19027`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19027) |
| `la_norm_6d_to_5d_err_char_w` | function | [`src/la_norms.f90:19126`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19126) |
| `la_norm_7d_to_6d_err_char_w` | function | [`src/la_norms.f90:19227`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19227) |
| `matrix_norm_char_w` | function | [`src/la_norms.f90:19316`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19316) |
| `matrix_norm_3d_to_1d_char_w` | function | [`src/la_norms.f90:19366`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19366) |
| `matrix_norm_4d_to_2d_char_w` | function | [`src/la_norms.f90:19465`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19465) |
| `matrix_norm_5d_to_3d_char_w` | function | [`src/la_norms.f90:19565`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19565) |
| `matrix_norm_6d_to_4d_char_w` | function | [`src/la_norms.f90:19666`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19666) |
| `matrix_norm_7d_to_5d_char_w` | function | [`src/la_norms.f90:19768`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19768) |
| `la_norm_1d_order_err_int_w` | function | [`src/la_norms.f90:19888`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19888) |
| `la_norm_2d_order_err_int_w` | function | [`src/la_norms.f90:19971`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L19971) |
| `la_norm_3d_order_err_int_w` | function | [`src/la_norms.f90:20054`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20054) |
| `la_norm_4d_order_err_int_w` | function | [`src/la_norms.f90:20137`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20137) |
| `la_norm_5d_order_err_int_w` | function | [`src/la_norms.f90:20220`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20220) |
| `la_norm_6d_order_err_int_w` | function | [`src/la_norms.f90:20303`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20303) |
| `la_norm_7d_order_err_int_w` | function | [`src/la_norms.f90:20386`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20386) |
| `la_norm_2d_to_1d_err_int_w` | function | [`src/la_norms.f90:20475`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20475) |
| `la_norm_3d_to_2d_err_int_w` | function | [`src/la_norms.f90:20571`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20571) |
| `la_norm_4d_to_3d_err_int_w` | function | [`src/la_norms.f90:20668`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20668) |
| `la_norm_5d_to_4d_err_int_w` | function | [`src/la_norms.f90:20767`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20767) |
| `la_norm_6d_to_5d_err_int_w` | function | [`src/la_norms.f90:20866`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20866) |
| `la_norm_7d_to_6d_err_int_w` | function | [`src/la_norms.f90:20967`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L20967) |
| `matrix_norm_int_w` | function | [`src/la_norms.f90:21056`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21056) |
| `matrix_norm_3d_to_1d_int_w` | function | [`src/la_norms.f90:21106`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21106) |
| `matrix_norm_4d_to_2d_int_w` | function | [`src/la_norms.f90:21205`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21205) |
| `matrix_norm_5d_to_3d_int_w` | function | [`src/la_norms.f90:21305`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21305) |
| `matrix_norm_6d_to_4d_int_w` | function | [`src/la_norms.f90:21406`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21406) |
| `matrix_norm_7d_to_5d_int_w` | function | [`src/la_norms.f90:21508`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_norms.f90#L21508) |
| `la_pseudoinvert_s` | subroutine | [`src/la_pinv.f90:173`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L173) |
| `la_pseudoinverse_d` | function | [`src/la_pinv.f90:337`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L337) |
| `la_pseudoinvert_q` | subroutine | [`src/la_pinv.f90:370`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L370) |
| `la_pseudoinvert_c` | subroutine | [`src/la_pinv.f90:469`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L469) |
| `la_pseudoinverse_z` | function | [`src/la_pinv.f90:633`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L633) |
| `la_pseudoinvert_w` | subroutine | [`src/la_pinv.f90:666`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_pinv.f90#L666) |
| `get_schur_s_workspace` | subroutine | [`src/la_schur.f90:144`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L144) |
| `get_schur_q_workspace` | subroutine | [`src/la_schur.f90:648`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L648) |
| `get_schur_c_workspace` | subroutine | [`src/la_schur.f90:900`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L900) |
| `get_schur_w_workspace` | subroutine | [`src/la_schur.f90:1400`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_schur.f90#L1400) |
| `la_ssolve_one` | function | [`src/la_solve.f90:78`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L78) |
| `la_dsolve_one` | function | [`src/la_solve.f90:146`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L146) |
| `la_qsolve_one` | function | [`src/la_solve.f90:214`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L214) |
| `la_csolve_one` | function | [`src/la_solve.f90:282`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L282) |
| `la_zsolve_one` | function | [`src/la_solve.f90:350`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L350) |
| `la_wsolve_one` | function | [`src/la_solve.f90:418`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L418) |
| `la_ssolve_multiple` | function | [`src/la_solve.f90:486`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L486) |
| `la_dsolve_multiple` | function | [`src/la_solve.f90:554`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L554) |
| `la_qsolve_multiple` | function | [`src/la_solve.f90:622`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L622) |
| `la_csolve_multiple` | function | [`src/la_solve.f90:690`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L690) |
| `la_zsolve_multiple` | function | [`src/la_solve.f90:758`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L758) |
| `la_wsolve_multiple` | function | [`src/la_solve.f90:826`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_solve.f90#L826) |
| `la_svd_s` | subroutine | [`src/la_svd.f90:143`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L143) |
| `la_svdvals_d` | function | [`src/la_svd.f90:302`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L302) |
| `la_svd_q` | subroutine | [`src/la_svd.f90:517`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L517) |
| `la_svd_c` | subroutine | [`src/la_svd.f90:704`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L704) |
| `la_svdvals_z` | function | [`src/la_svd.f90:869`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L869) |
| `la_svd_w` | subroutine | [`src/la_svd.f90:1090`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_svd.f90#L1090) |

## Non-pure interface declarations

These declarations are kept separate because they may describe external implementations rather than code defined in this repository.

| Procedure | Kind | Source |
|---|---|---|
| `cgees` | subroutine | [`src/la_lapack.f90:1230`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1230) |
| `sgees` | subroutine | [`src/la_lapack.f90:1264`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1264) |
| `cgeev` | subroutine | [`src/la_lapack.f90:1311`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1311) |
| `sgeev` | subroutine | [`src/la_lapack.f90:1341`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1341) |
| `cgels` | subroutine | [`src/la_lapack.f90:1750`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1750) |
| `sgels` | subroutine | [`src/la_lapack.f90:1777`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1777) |
| `cgelsd` | subroutine | [`src/la_lapack.f90:1832`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1832) |
| `sgelsd` | subroutine | [`src/la_lapack.f90:1862`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1862) |
| `cgelss` | subroutine | [`src/la_lapack.f90:1907`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1907) |
| `sgelss` | subroutine | [`src/la_lapack.f90:1937`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L1937) |
| `cgelsy` | subroutine | [`src/la_lapack.f90:2002`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L2002) |
| `sgelsy` | subroutine | [`src/la_lapack.f90:2034`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L2034) |
| `cgesdd` | subroutine | [`src/la_lapack.f90:2967`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L2967) |
| `sgesdd` | subroutine | [`src/la_lapack.f90:2997`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L2997) |
| `cgesvd` | subroutine | [`src/la_lapack.f90:3099`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3099) |
| `sgesvd` | subroutine | [`src/la_lapack.f90:3129`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3129) |
| `cgesvdq` | subroutine | [`src/la_lapack.f90:3171`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3171) |
| `sgesvdq` | subroutine | [`src/la_lapack.f90:3203`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3203) |
| `cgetsls` | subroutine | [`src/la_lapack.f90:3571`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3571) |
| `sgetsls` | subroutine | [`src/la_lapack.f90:3598`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3598) |
| `cgges` | subroutine | [`src/la_lapack.f90:3852`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3852) |
| `dgges` | subroutine | [`src/la_lapack.f90:3870`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3870) |
| `sgges` | subroutine | [`src/la_lapack.f90:3888`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3888) |
| `zgges` | subroutine | [`src/la_lapack.f90:3906`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3906) |
| `cggev` | subroutine | [`src/la_lapack.f90:3942`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3942) |
| `dggev` | subroutine | [`src/la_lapack.f90:3958`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3958) |
| `sggev` | subroutine | [`src/la_lapack.f90:3974`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3974) |
| `zggev` | subroutine | [`src/la_lapack.f90:3990`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L3990) |
| `chbev` | subroutine | [`src/la_lapack.f90:4901`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L4901) |
| `zhbev` | subroutine | [`src/la_lapack.f90:4917`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L4917) |
| `chbevd` | subroutine | [`src/la_lapack.f90:4944`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L4944) |
| `zhbevd` | subroutine | [`src/la_lapack.f90:4960`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L4960) |
| `cheev` | subroutine | [`src/la_lapack.f90:5262`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5262) |
| `zheev` | subroutine | [`src/la_lapack.f90:5277`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5277) |
| `cheevd` | subroutine | [`src/la_lapack.f90:5303`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5303) |
| `zheevd` | subroutine | [`src/la_lapack.f90:5319`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5319) |
| `cheevr` | subroutine | [`src/la_lapack.f90:5387`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5387) |
| `zheevr` | subroutine | [`src/la_lapack.f90:5404`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5404) |
| `chegv` | subroutine | [`src/la_lapack.f90:5463`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5463) |
| `zhegv` | subroutine | [`src/la_lapack.f90:5479`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5479) |
| `chegvd` | subroutine | [`src/la_lapack.f90:5508`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5508) |
| `zhegvd` | subroutine | [`src/la_lapack.f90:5524`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L5524) |
| `chgeqz` | subroutine | [`src/la_lapack.f90:6432`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6432) |
| `dhgeqz` | subroutine | [`src/la_lapack.f90:6447`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6447) |
| `shgeqz` | subroutine | [`src/la_lapack.f90:6462`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6462) |
| `zhgeqz` | subroutine | [`src/la_lapack.f90:6477`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6477) |
| `chpev` | subroutine | [`src/la_lapack.f90:6536`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6536) |
| `zhpev` | subroutine | [`src/la_lapack.f90:6551`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6551) |
| `chpevd` | subroutine | [`src/la_lapack.f90:6577`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6577) |
| `zhpevd` | subroutine | [`src/la_lapack.f90:6593`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6593) |
| `chpgv` | subroutine | [`src/la_lapack.f90:6653`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6653) |
| `zhpgv` | subroutine | [`src/la_lapack.f90:6669`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6669) |
| `chpgvd` | subroutine | [`src/la_lapack.f90:6699`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6699) |
| `zhpgvd` | subroutine | [`src/la_lapack.f90:6715`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6715) |
| `chsein` | subroutine | [`src/la_lapack.f90:6953`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6953) |
| `dhsein` | subroutine | [`src/la_lapack.f90:6970`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6970) |
| `shsein` | subroutine | [`src/la_lapack.f90:6987`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L6987) |
| `zhsein` | subroutine | [`src/la_lapack.f90:7004`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7004) |
| `dhseqr` | subroutine | [`src/la_lapack.f90:7046`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7046) |
| `shseqr` | subroutine | [`src/la_lapack.f90:7061`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7061) |
| `dla_gbrcond` | function | [`src/la_lapack.f90:7195`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7195) |
| `sla_gbrcond` | function | [`src/la_lapack.f90:7210`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7210) |
| `cla_gbrcond_c` | function | [`src/la_lapack.f90:7229`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7229) |
| `zla_gbrcond_c` | function | [`src/la_lapack.f90:7247`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7247) |
| `dla_gercond` | function | [`src/la_lapack.f90:7395`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7395) |
| `sla_gercond` | function | [`src/la_lapack.f90:7410`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7410) |
| `cla_gercond_c` | function | [`src/la_lapack.f90:7429`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7429) |
| `zla_gercond_c` | function | [`src/la_lapack.f90:7447`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7447) |
| `cla_hercond_c` | function | [`src/la_lapack.f90:7560`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7560) |
| `zla_hercond_c` | function | [`src/la_lapack.f90:7578`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7578) |
| `cla_herpvgrw` | function | [`src/la_lapack.f90:7604`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7604) |
| `zla_herpvgrw` | function | [`src/la_lapack.f90:7618`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7618) |
| `dla_porcond` | function | [`src/la_lapack.f90:7699`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7699) |
| `sla_porcond` | function | [`src/la_lapack.f90:7714`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7714) |
| `cla_porcond_c` | function | [`src/la_lapack.f90:7733`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7733) |
| `zla_porcond_c` | function | [`src/la_lapack.f90:7751`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7751) |
| `cla_porpvgrw` | function | [`src/la_lapack.f90:7777`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7777) |
| `dla_porpvgrw` | function | [`src/la_lapack.f90:7789`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7789) |
| `sla_porpvgrw` | function | [`src/la_lapack.f90:7802`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7802) |
| `zla_porpvgrw` | function | [`src/la_lapack.f90:7815`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7815) |
| `dla_syrcond` | function | [`src/la_lapack.f90:7902`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7902) |
| `sla_syrcond` | function | [`src/la_lapack.f90:7917`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7917) |
| `cla_syrcond_c` | function | [`src/la_lapack.f90:7936`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7936) |
| `zla_syrcond_c` | function | [`src/la_lapack.f90:7954`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7954) |
| `cla_syrpvgrw` | function | [`src/la_lapack.f90:7980`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7980) |
| `dla_syrpvgrw` | function | [`src/la_lapack.f90:7993`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L7993) |
| `sla_syrpvgrw` | function | [`src/la_lapack.f90:8007`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8007) |
| `zla_syrpvgrw` | function | [`src/la_lapack.f90:8021`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8021) |
| `clacon` | subroutine | [`src/la_lapack.f90:8204`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8204) |
| `dlacon` | subroutine | [`src/la_lapack.f90:8217`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8217) |
| `slacon` | subroutine | [`src/la_lapack.f90:8231`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8231) |
| `zlacon` | subroutine | [`src/la_lapack.f90:8245`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L8245) |
| `dlaexc` | subroutine | [`src/la_lapack.f90:9141`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L9141) |
| `slaexc` | subroutine | [`src/la_lapack.f90:9155`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L9155) |
| `clangb` | function | [`src/la_lapack.f90:10126`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10126) |
| `dlangb` | function | [`src/la_lapack.f90:10138`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10138) |
| `slangb` | function | [`src/la_lapack.f90:10151`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10151) |
| `zlangb` | function | [`src/la_lapack.f90:10164`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10164) |
| `clange` | function | [`src/la_lapack.f90:10182`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10182) |
| `slange` | function | [`src/la_lapack.f90:10207`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10207) |
| `clanhb` | function | [`src/la_lapack.f90:10290`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10290) |
| `zlanhb` | function | [`src/la_lapack.f90:10303`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10303) |
| `clanhe` | function | [`src/la_lapack.f90:10321`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10321) |
| `zlanhe` | function | [`src/la_lapack.f90:10334`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10334) |
| `clanhf` | function | [`src/la_lapack.f90:10352`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10352) |
| `zlanhf` | function | [`src/la_lapack.f90:10365`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10365) |
| `clanhp` | function | [`src/la_lapack.f90:10383`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10383) |
| `zlanhp` | function | [`src/la_lapack.f90:10396`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10396) |
| `clanhs` | function | [`src/la_lapack.f90:10414`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10414) |
| `dlanhs` | function | [`src/la_lapack.f90:10426`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10426) |
| `slanhs` | function | [`src/la_lapack.f90:10439`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10439) |
| `zlanhs` | function | [`src/la_lapack.f90:10452`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10452) |
| `clansb` | function | [`src/la_lapack.f90:10501`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10501) |
| `dlansb` | function | [`src/la_lapack.f90:10513`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10513) |
| `slansb` | function | [`src/la_lapack.f90:10526`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10526) |
| `zlansb` | function | [`src/la_lapack.f90:10539`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10539) |
| `dlansf` | function | [`src/la_lapack.f90:10557`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10557) |
| `slansf` | function | [`src/la_lapack.f90:10570`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10570) |
| `clansp` | function | [`src/la_lapack.f90:10588`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10588) |
| `dlansp` | function | [`src/la_lapack.f90:10600`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10600) |
| `slansp` | function | [`src/la_lapack.f90:10613`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10613) |
| `zlansp` | function | [`src/la_lapack.f90:10626`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10626) |
| `clansy` | function | [`src/la_lapack.f90:10673`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10673) |
| `slansy` | function | [`src/la_lapack.f90:10698`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10698) |
| `zlansy` | function | [`src/la_lapack.f90:10711`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10711) |
| `clantb` | function | [`src/la_lapack.f90:10729`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10729) |
| `dlantb` | function | [`src/la_lapack.f90:10742`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10742) |
| `slantb` | function | [`src/la_lapack.f90:10755`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10755) |
| `zlantb` | function | [`src/la_lapack.f90:10769`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10769) |
| `clantp` | function | [`src/la_lapack.f90:10787`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10787) |
| `dlantp` | function | [`src/la_lapack.f90:10799`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10799) |
| `slantp` | function | [`src/la_lapack.f90:10812`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10812) |
| `zlantp` | function | [`src/la_lapack.f90:10825`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10825) |
| `clantr` | function | [`src/la_lapack.f90:10843`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10843) |
| `dlantr` | function | [`src/la_lapack.f90:10855`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10855) |
| `slantr` | function | [`src/la_lapack.f90:10868`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10868) |
| `zlantr` | function | [`src/la_lapack.f90:10881`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L10881) |
| `dlaqr0` | subroutine | [`src/la_lapack.f90:11512`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L11512) |
| `slaqr0` | subroutine | [`src/la_lapack.f90:11527`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L11527) |
| `dlaqr4` | subroutine | [`src/la_lapack.f90:11642`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L11642) |
| `slaqr4` | subroutine | [`src/la_lapack.f90:11657`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L11657) |
| `slaqtr` | subroutine | [`src/la_lapack.f90:11962`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L11962) |
| `claqz0` | subroutine | [`src/la_lapack.f90:12019`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L12019) |
| `dlaqz0` | subroutine | [`src/la_lapack.f90:12034`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L12034) |
| `slaqz0` | subroutine | [`src/la_lapack.f90:12049`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L12049) |
| `zlaqz0` | subroutine | [`src/la_lapack.f90:12064`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L12064) |
| `dsbev` | subroutine | [`src/la_lapack.f90:19246`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19246) |
| `ssbev` | subroutine | [`src/la_lapack.f90:19260`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19260) |
| `dsbevd` | subroutine | [`src/la_lapack.f90:19285`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19285) |
| `ssbevd` | subroutine | [`src/la_lapack.f90:19300`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19300) |
| `dspev` | subroutine | [`src/la_lapack.f90:19576`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19576) |
| `sspev` | subroutine | [`src/la_lapack.f90:19590`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19590) |
| `dspevd` | subroutine | [`src/la_lapack.f90:19615`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19615) |
| `sspevd` | subroutine | [`src/la_lapack.f90:19630`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19630) |
| `dspgv` | subroutine | [`src/la_lapack.f90:19689`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19689) |
| `sspgv` | subroutine | [`src/la_lapack.f90:19703`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19703) |
| `dspgvd` | subroutine | [`src/la_lapack.f90:19731`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19731) |
| `sspgvd` | subroutine | [`src/la_lapack.f90:19746`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L19746) |
| `ssyev` | subroutine | [`src/la_lapack.f90:21232`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L21232) |
| `ssyevd` | subroutine | [`src/la_lapack.f90:21274`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L21274) |
| `ssyevr` | subroutine | [`src/la_lapack.f90:21357`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L21357) |
| `ssygv` | subroutine | [`src/la_lapack.f90:21432`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L21432) |
| `ssygvd` | subroutine | [`src/la_lapack.f90:21475`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L21475) |
| `ctbcon` | subroutine | [`src/la_lapack.f90:22900`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L22900) |
| `dtbcon` | subroutine | [`src/la_lapack.f90:22915`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L22915) |
| `stbcon` | subroutine | [`src/la_lapack.f90:22930`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L22930) |
| `ztbcon` | subroutine | [`src/la_lapack.f90:22945`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L22945) |
| `ctpcon` | subroutine | [`src/la_lapack.f90:23887`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L23887) |
| `dtpcon` | subroutine | [`src/la_lapack.f90:23901`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L23901) |
| `stpcon` | subroutine | [`src/la_lapack.f90:23915`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L23915) |
| `ztpcon` | subroutine | [`src/la_lapack.f90:23929`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L23929) |
| `ctrcon` | subroutine | [`src/la_lapack.f90:24682`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24682) |
| `dtrcon` | subroutine | [`src/la_lapack.f90:24696`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24696) |
| `strcon` | subroutine | [`src/la_lapack.f90:24710`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24710) |
| `ztrcon` | subroutine | [`src/la_lapack.f90:24724`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24724) |
| `dtrexc` | subroutine | [`src/la_lapack.f90:24928`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24928) |
| `strexc` | subroutine | [`src/la_lapack.f90:24943`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L24943) |
| `ctrsen` | subroutine | [`src/la_lapack.f90:25049`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25049) |
| `dtrsen` | subroutine | [`src/la_lapack.f90:25065`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25065) |
| `strsen` | subroutine | [`src/la_lapack.f90:25081`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25081) |
| `strsna` | subroutine | [`src/la_lapack.f90:25151`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25151) |
| `ctrsyl` | subroutine | [`src/la_lapack.f90:25193`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25193) |
| `dtrsyl` | subroutine | [`src/la_lapack.f90:25208`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25208) |
| `strsyl` | subroutine | [`src/la_lapack.f90:25224`](https://github.com/Beliavsky/fortran-lapack/blob/45d2e9b11dface3fd94c2cb2dfece934aee74436/src/la_lapack.f90#L25224) |

## Remaining implementations by file

| Source file | Count |
|---|---:|
| `src/la_norms.f90` | 228 |
| `src/la_lapack_q.f90` | 78 |
| `src/la_lapack_s.f90` | 76 |
| `src/la_lapack_w.f90` | 76 |
| `src/la_lapack_c.f90` | 74 |
| `src/la_lapack_z.f90` | 60 |
| `src/la_eigs.f90` | 54 |
| `src/la_lapack_d.f90` | 42 |
| `src/la_eye.f90` | 18 |
| `src/la_pinv.f90` | 14 |
| `src/la_least_squares.f90` | 12 |
| `src/la_schur.f90` | 12 |
| `src/la_solve.f90` | 12 |
| `src/la_svd.f90` | 10 |
| `src/la_determinant.f90` | 6 |
| `src/la_inverse.f90` | 6 |
