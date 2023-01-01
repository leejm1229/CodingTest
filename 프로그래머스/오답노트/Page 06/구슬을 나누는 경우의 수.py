'''
balls	share	result
3	    2	    3
5	    3	    10
'''
from math import comb

def solution(balls, share):
    return comb(balls, share)