Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(-3.5)
3.5
all([1, 2, 3, 4])
True
all([4, -2, 0.0, 4])
False
any([1, 2, 3, 4])
True
any([4, -2, 0.0, 4])
True
chr(97)
'a'
chr(48)
'0'
ord('a')
97
ord('0')
48
dir([1, 2, 3])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir({'1':'a'})
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dir(1)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
divomod(7, 3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    divomod(7, 3)
NameError: name 'divomod' is not defined. Did you mean: 'divmod'?
divmod(7, 3)
(2, 1)
divmod(1.3, 0.2)
(6.0, 0.09999999999999998)
oct(8)
'0o10'
oct(234)
'0o352'
hex(16)
'0x10'
hex(234)
'0xea'
a = 3
id(a)
140715885267448
int('3')
3
str(3)
'3'
list("Python")
['P', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3))
[1, 2, 3]
tuple("Python")
('P', 'y', 't', 'h', 'o', 'n')
tuple([1, 2, 3])
(1, 2, 3)
type("abc")
<class 'str'>
type(a)
<class 'int'>
sum = lamda a, b:a+b
SyntaxError: invalid syntax
sum = lambda a,b: a+b
sum
<function <lambda> at 0x0000016E8C238040>
sum(3, 5)
8
max([1, 4, 2, 8, 6])
8
max("Python")
'y'
min([1, 4, 2, 8, 6])
1
>>> min("Python")
'P'
>>> pow(2, 4)
16
>>> c = input()
21
>>> c
'21'
>>> c = input("정수를 입력하세요: ")
정수를 입력하세요: 21
>>> ㅊ
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    ㅊ
NameError: name 'ᄎ' is not defined
>>> c
'21'
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(5, 10))
[5, 6, 7, 8, 9]
>>> list(range(5, 10, 2))
[5, 7, 9]
>>> len('Python')
6
>>> sorted([3, 0, 2, 1])
[0, 1, 2, 3]
>>> sorted('Python')
['P', 'h', 'n', 'o', 't', 'y']
>>> Request('http://www.hanb.co.kr')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Request('http://www.hanb.co.kr')
NameError: name 'Request' is not defined
>>> import urllib.request
>>> urllib.request.Request('http://www.hanb.co.kr')
<urllib.request.Request object at 0x0000016E8C21E450>
>>> import panddas
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    import panddas
ModuleNotFoundError: No module named 'panddas'
>>> import pandas
pandas
>>> pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2024, 10, 15, 20, 35, 53, 737638)
