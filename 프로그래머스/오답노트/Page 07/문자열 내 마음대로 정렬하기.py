'''
strings	                    n	    return
["sun", "bed", "car"]	    1	    ["car", "bed", "sun"]
["abce", "abcd", "cdx"]	    2	    ["abcd", "abce", "cdx"]
'''
# 람다안에 튜플을 넣어줌으로써 sort의 우선순위를 정할 수 있다.
# 비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.
def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))
