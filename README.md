# PL 수업 시간에 사용된 간단한 코드 모음

## Run?
- WSL2 기반의 Ubuntu 22.04.3에서 실행
```bash
$ sudo apt install gfortran
$ gfortran --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$ gfortran -o merge-sort-fotrlan ./week02/merge-sort.f95

$ sudo apt install sbcl
$ sbcl --script ./week02/merge-sort.lisp

$ sudo apt install swi-prolog-core
$ swipl -s ./week02/merge-sort.pl
?- read(Xs), mergesort(Xs,S).
|: [10, 11, 12, 13, 14, 5, 4, 3, 2, 1].

Xs = [10, 11, 12, 13, 14, 5, 4, 3, 2|...],
S = [1, 2, 3, 4, 5, 10, 11, 12, 13|...] .
```