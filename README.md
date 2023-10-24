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
