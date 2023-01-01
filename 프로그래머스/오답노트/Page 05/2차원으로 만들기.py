'''
num_list	                n	            result
[1, 2, 3, 4, 5, 6, 7, 8]	2	    [[1, 2], [3, 4], [5, 6], [7, 8]]
'''
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()