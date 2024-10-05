## Problem Solving From 2023  

### Python Notes  
timeout solution:  
If you use input() many times(like 1_000_000),  
you MUST use sys.stdin.readline for input  
(the lesson from BOJ 15917)  
sys.stdin.readline() includes '\n' in the end of the input line,  
unlike print() does not  
  
<strong>import sys</strong>  
<strong>input = sys.stdin.readline</strong>  

more:  
You can use sys.stdout.write("string\n"), instead of print("string")  
  
import sys  
<strong>sys.stdout.write("string\n")</strong>  
  
layer:  
Make a copy of mutable data before use(deep copy)  
<strong>import copy</strong>  
<strong>b = copy.deepcopy(a)</strong>  
  
If you don't want to change the original data,  
make a sorted copy  
Use <strong>b = sorted(a)</strong> instead of a.sort()  
  
more:  
To make a <strong>multi-dimensional list</strong>,  
<strong>do not use shallow copy</strong>, it will make an error  
\>\>\> a = [[1] * 3] * 3  
\>\>\> a  
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]  
\>\>\> a[0][1] = 2  
\>\>\> a  
[[1, 2, 1], [1, 2, 1], [1, 2, 1]]  
  
<strong>Use list comprehension</strong>  
\>\>\> <strong>a = [[1 for i in range(3)] for j in range(3)]</strong>  
\>\>\> a  
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]  
\>\>\> a[0][1] = 2  
\>\>\> a  
[[1, 2, 1], [1, 1, 1], [1, 1, 1]]  
  
recursion limit:  
<strong>import sys</strong>  
<strong>print(sys.getrecursionlimit()) # 1000</strong>  
<strong>print(sys.setrecursionlimit(1_000_000))</strong>  
  