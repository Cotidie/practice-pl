# BNF/EBNF를 사용한 간단한 DSL 만들기

## 실행

```python
$ python -m venv venv
$ .venv\Scripts\activate
(venv) $ pip install ply numpy
(venv) $ python pyyacc.py
>>> 1+2
3
>>> 2^10
1024
>>> prefix(2+1*3)  
+2*13
>>> 2/0
Can't divide by 0
(venv) $ python pyvector-dsl.py
>>> vector v1 = [1, 2, 3]
None
>>> vector v2 = [4, 5, 6]
None
>>> vector v3 = v1 + v2
None
>>> print(v3)
[5 7 9]
None
>>> matrix m1 = [[1, 2], [3, 4], [5, 6]]
None
>>> matrix m2 = [[5, 6, 7], [7, 8, 9]]
None
>>> matrix m3 = m1 * m2
None
>>> print(m3)
[[19 22 25]
 [43 50 57]
 [67 78 89]]
None
```