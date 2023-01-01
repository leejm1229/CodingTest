# 배열에서 원소 개수 찾기

def solution(array, height):
    array.append(height)
    array.sort(reverse = True)
    answer = array.index(height)
    
    return answer