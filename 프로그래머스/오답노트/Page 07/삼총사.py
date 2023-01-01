'''
number	                    result
[-2, 3, 0, 2, -5]	        2
[-3, -2, -1, 0, 1, 2, 3]	5
[-1, 1, -1, 1]	            0
'''

from itertools import combinations # 조합 

def solution(number):
    answer = 0
    for i in combinations(number, 3): 
        if sum(i) == 0 : 
            answer += 1 
    
    return answer 