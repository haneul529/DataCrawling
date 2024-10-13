Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 123
a = 12.34
a
12.34
a = 1 + 2j
a
(1+2j)
a.real
1.0
a.imag
2.0
a.conjugate()
(1-2j)
abs(a)
2.23606797749979
a = 3
b = 4
a + b
7
a - b
-1
a*b
12
a/b
0.75
a**b
81
2**3
8
a%b
3
7%3
1
a//b
0
7//3
2
s1 = 'Hello Python'
s1
'Hello Python'
s2 = "Hello Python"
s2
'Hello Python'
s3 = '''Hello Python'''
s3
'Hello Python'
s4 = """Hello Python"""
s4
'Hello Python'
head = "Python"
tail = " is fun"
head + tail
'Python is fun'
head*2
'PythonPython'
print("="*5)
=====
a = "Now is better than never"
a[0]
'N'
a[4]
'i'
a[-]
SyntaxError: invalid syntax
a[-1]
'r'
a[-2]
'e'
b = a[0] + a[1] + a[2]
b
'Now'
a[0:3]
'Now'
a[4:6]
'is'
a[19:]
'never'
a[:3]
'Now'
a[:]
'Now is better than never'
a[7:-11]
'better'
a = "Python"
a.count('p')
0
a.find('y')
1
a
.find('p')
SyntaxError: invalid syntax
a.find('p')
-1
a.index('p')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.index('p')
ValueError: substring not found
a.index('y')
1
b = ","
c = b.join('Abcd')
c
'A,b,c,d'
a,upper()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,upper()
NameError: name 'upper' is not defined. Did you mean: 'super'?
a.upper()
'PYTHON'
a.lower()
'python'
d = "    py    "
d.lstrip()
'py    '
d.rstrip()
'    py'
d.strip()
'py'
a = 'Pithon'
a[1] = 'y'
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a[1] = 'y'
TypeError: 'str' object does not support item assignment
a = "Python is difficult."
a.replace("difficult", "funny")
'Python is funny.'
a.split()
['Python', 'is', 'difficult.']
b = "a, b, c, d"
b
'a, b, c, d'
b.split(',')
['a', ' b', ' c', ' d']
a = [1, 2, 3]
b = ['Life', 'is', 'too', 'short']
c = [1, 2, 'Life', 'is']
d = [1, 2, [3, 4], ['Life', 'is']]
d[0]
1
d[2]
[3, 4]
d[3]
['Life', 'is']
d[3][-1]
'is'
d[0:3]
[1, 2, [3, 4]]
a+b
[1, 2, 3, 'Life', 'is', 'too', 'short']
b[0] + " hi~^^;"
'Life hi~^^;'
a[0] + " hi~^^;"
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a[0] + " hi~^^;"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
a * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a[2] = 99
a[1:2]
[2]
a[1:2] = ['a', 'b', 'c']
a
[1, 'a', 'b', 'c', 99]
a[-1] = ['d', 'e', 'f']
a
[1, 'a', 'b', 'c', ['d', 'e', 'f']]
del a[-1]
a
[1, 'a', 'b', 'c']
a.append(5)
a
[1, 'a', 'b', 'c', 5]
b.sort()
b
['Life', 'is', 'short', 'too']
a = [3, 4, 1, 9]
a.reverse()
a
[9, 1, 4, 3]
a.index(9)
0
a.insert(0, 99)
a
[99, 9, 1, 4, 3]
a.remove(99)
a
[9, 1, 4, 3]
a.remove(99)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.remove(99)
ValueError: list.remove(x): x not in list
b = [1, 2, 3]
b.pop
<built-in method pop of list object at 0x0000023FA0865700>
b.pop()
3
b
[1, 2]
b.pop(0)
1
b
[2]
a = [2, 1, 0, 2, 3, 2, 4, 2]
a.count(2)
4
t1 = (1, )
t2 = (1, 2, 3)
t3 = 1, 2, 3
t4 = (1, 2, (3, 4), ('Life', 'is'))
t4[0]
1
t4[3][-1]
'is'
t4[0:3]
(1, 2, (3, 4))
t1 + t2
(1, 1, 2, 3)
t2 * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t2[2] = 99
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    t2[2] = 99
TypeError: 'tuple' object does not support item assignment
dic = {'name':'Hong', 'phone':'01012345678', 'birth': '0814', 1:'a'}
dic['pet'] = 'dog'
dic
{'name': 'Hong', 'phone': '01012345678', 'birth': '0814', 1: 'a', 'pet': 'dog'}
del dic[1]
dic
{'name': 'Hong', 'phone': '01012345678', 'birth': '0814', 'pet': 'dog'}
dic['pet']
'dog'
dic['name']
'Hong'
dic.keys()
dict_keys(['name', 'phone', 'birth', 'pet'])
list(dic.keys())
['name', 'phone', 'birth', 'pet']
dic.values()
dict_values(['Hong', '01012345678', '0814', 'dog'])
list(dic.values())
['Hong', '01012345678', '0814', 'dog']
dic.items()
dict_items([('name', 'Hong'), ('phone', '01012345678'), ('birth', '0814'), ('pet', 'dog')])
dic.clear()
dic
{}
s1 = {1, 2, 'a', 5}
s2 = set([1, 2, 3, 4, 5, 6])
s2
{1, 2, 3, 4, 5, 6}
s3 = set([4, 5, 6, 7, 8, 9])
s3
{4, 5, 6, 7, 8, 9}
s2 & s3
{4, 5, 6}
s2.intersection(s3)
{4, 5, 6}
s2 | s3
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s2.union(s3)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 - s3
{1, 2, 3}
s2.difference(s3)
{1, 2, 3}
s3.difference(s2)
{8, 9, 7}
s2.add(7)
s2
{1, 2, 3, 4, 5, 6, 7}
s2.update([6, 7, 8, 9, 10])
s2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2.remove(7)
s2
{1, 2, 3, 4, 5, 6, 8, 9, 10}
a = 'abc'
a
'abc'

a = ['a', 'b', 'c']
a
['a', 'b', 'c']
a = ('a', 'b', 'c')
a
('a', 'b', 'c')
a = {'name':"Hong"}
a
{'name': 'Hong'}
a = set(['a', 'b', 'c'])
a
{'c', 'b', 'a'}
a
{'c', 'b', 'a'}
x = 3
y = 2
x == y
False
x != y
True
x >= y
True
money = 1300
if money >= 1200 and money < 3500:
    print("버스를 탈 수 있습니다.")

    
버스를 탈 수 있습니다.
1 in [1, 2, 3]
True
x in [1, 2, 3]
True
x not in [1, 2, 3]
False
'a' in ('a', 'b', 'c', 'd')
True
'i' not in 'Python'
True
if money < 10:
    pass
else:
    print("저금하자!")

    
저금하자!
test_list = ['one', 'two', 'three']
for i in test_list:
    x = i + '!'
    print(x)

    
one!
two!
three!
number = 0
>>> for score in [90, 25, 67, 45, 93]:
...     number += 1
...     if score >= 60:
...         print("%d번 학생은 합격입니다." %number)
...         else:
...             
SyntaxError: invalid syntax
>>> for score in [90, 25, 67, 45, 93]:
...     number += 1
...     if score >= 60:
...         print("%d번 학생은 합격입니다." %number)
...     else:
...         print("%d번 학생은 불합격입니다." %number)
... 
...         
1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
>>> i = 0
>>> while i < 5:
...     i += 1
...     print('*' * i)
... 
...     
*
**
***
****
*****
>>> def sum1(a, b):
...     x = a+ b
...     return x
... 
>>> def sum2(*args):
...     x = 0
...     for i in args:
...         x += i
...     return x
... 
>>> a = 5
>>> b = 3
>>> sum1(a, b)
8
>>> sum(3, 5)
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    sum(3, 5)
TypeError: 'int' object is not iterable
>>> sum1(3, 5)
8
>>> sum2(1, 2, 3, 4, 5)
15
>>> sum2(2, 3.5, 10)
15.5
