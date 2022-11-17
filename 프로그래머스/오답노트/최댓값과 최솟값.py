# 리스트 안 요소의 타입을 변경

def solution(s):
    lst = list(map(int, s.split()))
    return ('{} {}'.format(min(lst), max(lst)))
