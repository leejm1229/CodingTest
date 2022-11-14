# 문자열 my_string이 매개변수로 주어질 때, 
# my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))