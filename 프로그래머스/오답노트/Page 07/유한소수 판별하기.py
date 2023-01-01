'''
a	    b	    result
7	    20	    1
11	    22	    1
12	    21	    2
'''
'''
1. 파이썬 gcd 함수 (최대공약수)
2. 파이썬 lcm 함수 (최소공배수) --> 3.9 버전부터
'''
from math import gcd 

def solution(a, b):
    b = b // gcd(a,b)
    
    while b%2 == 0:
        b = b // 2
        
    while b%5 == 0:
        b = b // 5
    
    if b == 1:
        return 1
    else:
        return 2
