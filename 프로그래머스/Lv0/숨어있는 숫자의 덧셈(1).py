# 문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 return
import re

def solution(my_string):
    answer = sum(map(int, list(re.sub('[^0-9]', '', my_string))))
    
    return answer