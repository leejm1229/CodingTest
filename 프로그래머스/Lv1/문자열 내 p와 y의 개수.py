# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return
# 대소문자 구분 X
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')