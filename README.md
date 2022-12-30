# nCk-Python

# Q2: nCk
Weight: 10%

Last update: 14 Nov, 10:00pm

Implement the Combinations by the formula of

```
_nC_k=_{n-1}C_{k-1}+_{n-1}C_k
n
​
 C 
k
​
 = 
n−1
​
 C 
k−1
​
 + 
n−1
​
 C 
k
​
 

where

_nC_0=_nC_n=1
n
​
 C 
0
​
 = 
n
​
 C 
n
​
 =1
```
using recursive function calls.  
Assume that user input n and k in the first 2 lines, report all combinations calculated in the process. 

For example, if user input n = 3 and k = 1, output:

```

3C1 = 2C0 + 2C1
2C0 = 1
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
3C1 = 3
Test cases.

Input:

4
2
Output:

4C2 = 3C1 + 3C2
3C1 = 2C0 + 2C1 
2C0 = 1
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
3C1 = 3
3C2 = 2C1 + 2C2
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
2C2 = 1
3C2 = 3
4C2 = 6
Input:

5
5
Output:

5C5 = 1

```
