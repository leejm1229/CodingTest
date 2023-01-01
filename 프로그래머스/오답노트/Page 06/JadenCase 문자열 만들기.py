'''
파이썬 문자열 capitalize()
문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
'''
def solution(s):
    answer = s.split(' ')
   
    for i in range(len(answer)):
        answer[i] = answer[i].capitalize()
   
    return ' '.join(answer)

'''
파이썬 title()
문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
'''
def Jaden_Case(s):
    
    return s.title()