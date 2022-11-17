'''
n	result
6	1
10	5
4	2
'''
def solution(n):
    pizza = 6
    box = 1
    while pizza%n != 0:
        pizza+=6
        box+=1
        
    return box

