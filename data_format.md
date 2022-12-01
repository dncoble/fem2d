Variables follow same names as given in the [FEM1D Input Description](https://highered.mheducation.com/sites/dl/free/0072466855/225647/InputdescrFEM1D.pdf). Not all data is relevant to every problem, and only relevant data must be included.

| Name | Type | Card | Notes |
|------|------|------|-------|
| `title` | string | 1 | has default value |
| `itype` | int | 2 | |
| `igrad` | int | 2 | one of 0 or 1 |
| `item` | int | 2 | one of 0, 1, or 2 |
| `neign` | int | 2 | one of 0, 1, or 2 |
| `nvalu` | int | 3 | has default value 0 |
| `nvctr` | int | 3 | has default value 0 |
| `ieltyp` | int | 4 | one of 0 or 1 |
| `npe` | int | 4 | |
| `mesh` | int | 4 | one of 0, 1, or 2 |
| `nprnt` | int | 4 | has default value 1 |
| `nem` | int | 5 | generated automatically |
| `nnm` | int | 5 | generated automatically |
| `nod` | list of coordinates | 6 | taken from `elem_connectivity` |
| `glxy` | list of list of int | 7 | taken from `node_coords` |
| `nrecl` | int | 8 | generated automatically |
| `nod1` | list of int | 9 | |
| `nodl` | list of int | 9 | |
| `nodinc` | list of int | 9 | |
| `x1 ` | list of float | 9 | |
| `y1` | list of float | 9 | |
| `xl` | list of float | 9 | |
| `yl` | list of float | 9 | |
| `ratio` | list of float | 9 | |
| `nrecel` | int | 10 | generated automatically |
| `nel1` | list of int | 11 | |
| `nell` | list of int | 11 | |
| `ielinc` | list of int | 11 | |
| `nodinc` | list of int | 11 | |
| `npe` | list of int | 11 | |
| `nodei` | list of list of int | 11 | |
| `nx` | int | 12 | generated automatically |
| `ny` | int | 12 | generated automatically |
| `x0` | float | 13 | |
| `dx` | list of float | 13 | |
| `y0` | float | 14 | |
| `dy` | list of float | 14 | |
| `nspv` | int | 15 | generated automatically |
| `ispv` | list of list of int | 16 | |
| `vspv` | list of float | 17 | |
| `nssv` | int | 18 | |
| `issv` | list of list of int | 19 | |
| `vssv` | list of float | 20 | |
| `a10` | float | 21 | |
| `a1x` | float | 21 | |
| `a1y` | float | 21 | |
| `a20` | float | 22 | |
| `a2x` | float | 22 | |
| `a2y` | float | 22 | |
| `a00` | float | 23 | |
| `inconv` | int | 24 | one of 0 or 1 |
| `nbe` | int | 25 | generated automatically |
| `ibn` | list of int | 26 | |
| `beta` | list of float | 26 | |
| `tinf` | list of float | 26 | |
| `inod` | list of list of int | 27 | |
| `viscity` | float | 28 | |
| `penalty` | float | 28 | |
| `lnstrs` | int | 29 | one of 0 or 1 |
| `e1` | float | 30, 31 | |
| `e2` | float | 30, 31 | |
| `anu12` | float | 30, 31 | |
| `g12` | float | 30, 31 | |
| `thkns` | float | 30, 31 | |
| `g13` | float | 31 | |
| `g23` | float | 31 | |
| `f0` | float | 32 | |
| `fx` | float | 32 | |
| `fy` | float | 32 | |
| `c0` | float | 33 | |
| `cx` | float | 33 | |
| `cy` | float | 33 | |
| `ntime` | int | 34 | |
| `nstp` | int | 34 | |
| `intvl` | int | 34 | |
| `intial` | int | 34 | one of 0 or 1 |
| `dt` | float | 35 | |
| `alfa` | float | 35 | |
| `gama` | float | 35 | |
| `epsln` | float | 35 | |
| `glu` | list of float | 36 | |
| `glv` | list of float | 37 | |
