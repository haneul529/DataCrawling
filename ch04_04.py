Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
f = open("C:\Users\lucia\OneDrive\바탕 화면\My_Python_Bhn/새파일.txt", 'w')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
f = open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt", 'w')
f
<_io.TextIOWrapper name='C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt' mode='w' encoding='cp949'>
f.close()
f = open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt", 'w')
for i in range(1, 6):
    data = "%d번째 줄입니다. \n"%i
    f.write(data)

    
11
11
11
11
11
f.close()
f=open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt",'a')
for i in range(6, 11):
    data = "%d번째 줄 추가입니다. \n"%i
    f.write(data)

    
14
14
14
14
15
f.close()
f=open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt",'r')
line = f.readline()
print(line)
1번째 줄입니다. 

while True:
    line = f.readline()
    if not line: break
    print(line)

    
2번째 줄입니다. 

3번째 줄입니다. 

4번째 줄입니다. 

5번째 줄입니다. 

6번째 줄 추가입니다. 

7번째 줄 추가입니다. 

8번째 줄 추가입니다. 

9번째 줄 추가입니다. 

10번째 줄 추가입니다. 

f.close()
f=open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt",'r')
lines = f.readlines()
print(lines)
['1번째 줄입니다. \n', '2번째 줄입니다. \n', '3번째 줄입니다. \n', '4번째 줄입니다. \n', '5번째 줄입니다. \n', '6번째 줄 추가입니다. \n', '7번째 줄 추가입니다. \n', '8번째 줄 추가입니다. \n', '9번째 줄 추가입니다. \n', '10번째 줄 추가입니다. \n']
for line in lines:
    print(line)

    
1번째 줄입니다. 

2번째 줄입니다. 

3번째 줄입니다. 

4번째 줄입니다. 

5번째 줄입니다. 

6번째 줄 추가입니다. 

7번째 줄 추가입니다. 

8번째 줄 추가입니다. 

9번째 줄 추가입니다. 

10번째 줄 추가입니다. 

f.close()
f=open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt",'r')
data = f.read()
data
'1번째 줄입니다. \n2번째 줄입니다. \n3번째 줄입니다. \n4번째 줄입니다. \n5번째 줄입니다. \n6번째 줄 추가입니다. \n7번째 줄 추가입니다. \n8번째 줄 추가입니다. \n9번째 줄 추가입니다. \n10번째 줄 추가입니다. \n'
f.close()
with open("C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/새파일.txt", 'w') as f:
    f.write("Now is better than never.")

    
25
data = f.read()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    data = f.read()
ValueError: I/O operation on closed file.
import numpy as np
np.__version__
'2.1.1'
ar1 = np.array([1, 2, 3, 4, 5])
ar1
array([1, 2, 3, 4, 5])
type(ar1)
<class 'numpy.ndarray'>
ar2 = np.array([[10, 20, 30], [40, 50, 60]])
ar2
array([[10, 20, 30],
       [40, 50, 60]])
ar3 = np.arange(1, 11, 2)
ar3
array([1, 3, 5, 7, 9])
ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2))
ar4
array([[1, 2],
       [3, 4],
       [5, 6]])
ar6 = ar2[0:2, 0:2]
ar6
array([[10, 20],
       [40, 50]])
ar7 = ar2[0, :]
ar7
array([10, 20, 30])
ar8 = ar1 + 10
ar8
array([11, 12, 13, 14, 15])
ar1 + ar8
array([12, 14, 16, 18, 20])
ar8 - ar1
array([10, 10, 10, 10, 10])
ar1 * 2
array([ 2,  4,  6,  8, 10])
ar1/2
array([0.5, 1. , 1.5, 2. , 2.5])
ar9 = np.dot(ar2, ar4)
ar9
array([[220, 280],
       [490, 640]])
import pandas as pd
pd.__version__
'2.2.2'
data1 = [10, 20, 30, 40, 50]
data1
[10, 20, 30, 40, 50]
data2 = ['1반', '2반', '3반', '4반', '5반']
data2
['1반', '2반', '3반', '4반', '5반']
sr1 = pd.Series(data1)
sr1
0    10
1    20
2    30
3    40
4    50
dtype: int64
sr2 = pd.Series(data2)
st2
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    st2
NameError: name 'st2' is not defined. Did you mean: 'sr2'?
sr2
0    1반
1    2반
2    3반
3    4반
4    5반
dtype: object
sr3 = pd.Series([101, 102, 103, 104, 105])
sr3
0    101
1    102
2    103
3    104
4    105
dtype: int64
sr4 = pd.Series(['월', '화', '수', '목', '금'])
sr4
0    월
1    화
2    수
3    목
4    금
dtype: object
sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
sr5
1000    10
1001    20
1002    30
1003    40
1004    50
dtype: int64
sr6 = pd.Series(data1, index = data2)
sr6
1반    10
2반    20
3반    30
4반    40
5반    50
dtype: int64
sr8[2]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sr8[2]
NameError: name 'sr8' is not defined. Did you mean: 'ar8'?
sr1 + sr3
0    111
1    122
2    133
3    144
4    155
dtype: int64
sr4 + sr2
0    월1반
1    화2반
2    수3반
3    목4반
4    금5반
dtype: object
data_dic = {}
data_dic = {
    'year':[2018, 2019, 2020],
    'sales':[350, 380, 1099]
    }
data_dic
{'year': [2018, 2019, 2020], 'sales': [350, 380, 1099]}
df1 = pd.DataFrame(data_dic)
dff1
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dff1
NameError: name 'dff1' is not defined. Did you mean: 'df1'?
df1
   year  sales
0  2018    350
1  2019    380
2  2020   1099
df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]], index = ['중간고사', '기말고사'], columns = data2[0:3])
df2
        1반    2반    3반
중간고사  89.2  92.5  90.8
기말고사  92.8  89.9  95.2
data_df = [['20201101', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
df3
          0     1   2   3
0  20201101  Hong  90  95
1  20201102   Kim  93  94
2  20201103   Lee  87  97
df3.columns = ['학번', '이름', '중간고사', '기말고사']
df3
         학번    이름 중간고사 기말고사
0  20201101  Hong   90   95
1  20201102   Kim   93   94
2  20201103   Lee   87   97
df3.head(2)
         학번    이름 중간고사 기말고사
0  20201101  Hong   90   95
1  20201102   Kim   93   94
df3.tail(2)
         학번   이름 중간고사 기말고사
1  20201102  Kim   93   94
2  20201103  Lee   87   97
df3['이름']
0    Hong
1     Kim
2     Lee
Name: 이름, dtype: object
df3.to_csv('C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/score.csv', header = 'False')
df4 = pd.read_csv('C:/Users/lucia/OneDrive/바탕 화면/My_Python_Bhn/score.csv', encoding='utf-8', index_col=0, engine='python')
df4
         학번    이름  중간고사  기말고사
0  20201101  Hong    90    95
1  20201102   Kim    93    94
2  20201103   Lee    87    97
import matplotlib
>>> matplotlib.__version__
'3.9.2'
>>> import matplotlib.pyplot as plt
>>> x = [2016, 2017, 2018, 2019, 2020]
>>> y = [350, 410, 520, 695, 543]
>>> plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x000001CF7266E720>]
>>> plt.title('Anual sales')
Text(0.5, 1.0, 'Anual sales')
>>> plt.xlabel('years')
Text(0.5, 0, 'years')
>>> plt.ylabel('sales')
Text(0, 0.5, 'sales')
>>> plt.show()
>>> y1 = [350, 410, 520, 695]
>>> y2 = [200, 250, 385, 350]
>>> x = range(len(y1))
>>> plt.bar(x, yq, width = 0.7, color = "blue")
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    plt.bar(x, yq, width = 0.7, color = "blue")
NameError: name 'yq' is not defined. Did you mean: 'y'?
>>> plt.bar(x, y1, width = 0.7, color = "blue")
<BarContainer object of 4 artists>
>>> plt.bar(x, y2, width = 0.7, color = "red")
<BarContainer object of 4 artists>
>>> plt.title('Quarterly sales')
Text(0.5, 1.0, 'Quarterly sales')
>>> plt.ylabel('sales')
Text(0, 0.5, 'sales')
>>> xLabel = ['first', 'second', 'third', 'fourth']
>>> plt.xticks(x, xLabel, fontsize = 10)
([<matplotlib.axis.XTick object at 0x000001CF726E0AD0>, <matplotlib.axis.XTick object at 0x000001CF726C71D0>, <matplotlib.axis.XTick object at 0x000001CF726B0AA0>, <matplotlib.axis.XTick object at 0x000001CF726C6A20>], [Text(0, 0, 'first'), Text(1, 0, 'second'), Text(2, 0, 'third'), Text(3, 0, 'fourth')])
>>> plt.legend(['chairs', 'desks'])
<matplotlib.legend.Legend object at 0x000001CF7266EC90>
>>> plt.show()
