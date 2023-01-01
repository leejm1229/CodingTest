'''
str.isdigit()

문자열이 '숫자'로만 이루어져있는지 확인하는 함수 입니다.

문자가 '단 하나'라도 있다면 False를 반환하고,
모든 문자가 '숫자'로만 이루어져있으면 True를 반환합니다.
'''
def solution(s):  
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False