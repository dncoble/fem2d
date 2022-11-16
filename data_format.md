Variables follow same names as given in the [FEM1D Input Description](https://highered.mheducation.com/sites/dl/free/0072466855/225647/InputdescrFEM1D.pdf). Not all data is relevant to every problem, and only relevant data must be included.

| Name | Type | Card | Notes |
|------|------|------|-------|
| `title` | string | 1 | has default value |
| `model` | int | 2 | one of 1, 2, 3, 4 |
| `ntype` | int | 2 | one of 0, 1, 2, or 3|
| `item` | int | 2 | one of 0, 1, 2, or 3|
| `ielem` | int | 3 | one of 0, 1, or 2|
| `nem` | int | 3 | generated automatically |
| `icont` | 0 | 4 | generated automatically, always 0 |
| `nprnt` | int | 4 | has default value |
| `nnm` | int | 10, 16 | generated automatically |
| `nod` | list of list of int | 11, 19, 21 | generated automatically |
| `glx` | list of float | 11 | |
| `ax0` | list of float | 12 | |
| `ax1` | list of float | 12 | |
| `bx0` | list of float | 13 | |
| `bx1` | list of float | 13 | |
| `cx0` | list of float | 14 | |
| `cx1` | list of float | 14 | |
| `fx0` | list of float | 15 | |
| `fx1` | list of float | 15 | |
| `fx2` | list of float | 15 | |
| `pr` | list of float | 17 | |
| `se` | list of float | 17 | |
| `sl` | list of float | 17 | |
| `sa` | list of float | 17 | |
| `si` | list of float | 17 | |
| `cs` | list of float | 17 | |
| `sn` | list of float | 17 | |
| `hf` | list of float | 18 | |
| `vf` | list of float | 18 | |
| `pf` | list of float | 18 | |
| `xb` | list of float | 18 | |
| `cnt` | list of float | 18 | |
| `snt` | list of float | 18 | |
| `se` | list of float | 20 | |
| `sl` | list of float | 20 | |
| `sa` | list of float | 20 | |
| `cs` | list of float | 20 | |
| `sn` | list of float | 20 | |
| `hf` | list of float | 20 | |
| `ncon` | int | 22 | generated automatically |
| `icon` | list of int | 23 | default empty list |
| `vcon` | list of float | 23 | default empty list |
| `nspv` | int | 24 | generated automatically |
| `ispv1` | list of int | 25 | default empty list |
| `ispv2` | list of int | 25 | default empty list |
| `vspv` | list of float | 25 | default empty list |
| `nssv` | int | 26 | generated automatically |
| `issv1` | list of int | 27 | default empty list |
| `issv2` | list of int | 27 | default empty list |
| `vssv` | list of float | 27 | default empty list |
| `nnbc` | int | 28 | generated automatically |
| `inbc1` | list of int | 29 | default empty list |
| `inbc2` | list of int | 29 | default empty list |
| `vnbc` | list of float | 29 | default empty list |
| `uref` | list of float | 29 | default empty list |
| `nmpc` | int | 30 | generated automatically |
| `imc11` | list of int | 31 | default empty list |
| `imc12` | list of int | 31 | default empty list |
| `imc21` | list of int | 31 | default empty list |
| `imc22` | list of int | 31 | default empty list |
| `vmpc` | list of float | 31 | default empty list |
| `vmpc4` | list of float | 31 | default empty list |
| `ct0` | float | 32 | |
| `ct1` | float | 33 | |
| `dt` | float | 33 | |
| `alfa` | float | 33 | |
| `gama` | float | 33 | |
| `incond` | int | 34 | one of 0 or 1|
| `ntime` | int | 34 | |
| `intvl` | int | 34 | |
| `guo` | list of float | 35 | |
| `gui` | list of float | 36 | |
