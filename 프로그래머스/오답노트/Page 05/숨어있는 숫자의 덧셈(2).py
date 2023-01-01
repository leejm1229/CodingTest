'''
my_string	       result
"aAb1B2cC34oOp"	    37
"1a2b3c4d123Z"	    133
'''

# 정규식을 이용하여 문자열 교체
# 리스트 빈 문자열인 원소 제거하기
# 리스트 각 타입의 요소 변경

import re
def solution(my_string):
    pattern = re.compile('[a-zA-Z]')
    my_string = re.sub(pattern, ' ', my_string).strip()
    my_string = my_string.split(' ')
    my_string = [x for x in my_string if x]
    answer = list(map(int, my_string))
    return sum(answer)