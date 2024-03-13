# Fortran, Lisp 그리고 Prolog를 사용한 Merge Sort 예제

## WLS2 설치
```
$ wsl --list -o
The following is a list of valid distributions that can be installed.
Install using 'wsl --install -d <Distro>'.

NAME                                   FRIENDLY NAME
Ubuntu                                 Ubuntu
Debian                                 Debian GNU/Linux
kali-linux                             Kali Linux Rolling
Ubuntu-18.04                           Ubuntu 18.04 LTS
Ubuntu-20.04                           Ubuntu 20.04 LTS
Ubuntu-22.04                           Ubuntu 22.04 LTS
OracleLinux_7_9                        Oracle Linux 7.9
OracleLinux_8_7                        Oracle Linux 8.7
OracleLinux_9_1                        Oracle Linux 9.1
openSUSE-Leap-15.5                     openSUSE Leap 15.5
SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
SUSE-Linux-Enterprise-15-SP5           SUSE Linux Enterprise 15 SP5
openSUSE-Tumbleweed                    openSUSE Tumbleweed

$ wsl --install -d Ubuntu
```

## WSL2 기반의 Ubuntu 22.04.3에서 실행
```bash
# fortran
$ sudo apt install gfortran
$ gfortran --version
GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
$ gfortran -o merge-sort-fotrlan ./week02/merge-sort.f95

# lisp
$ sudo apt install sbcl
$ sbcl --script ./week02/merge-sort.lisp

# prolog
$ sudo apt install swi-prolog-core
$ swipl -s ./week02/merge-sort.pl
?- read(Xs), mergesort(Xs,S).
|: [10, 11, 12, 13, 14, 5, 4, 3, 2, 1].
Xs = [10, 11, 12, 13, 14, 5, 4, 3, 2|...],
S = [1, 2, 3, 4, 5, 10, 11, 12, 13|...] .
```