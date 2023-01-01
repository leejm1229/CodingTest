'''
매개변수 x가 numlist 배열을 돌면서, 각 요소와의 차이를 절댓값 method인 abs로 구한다.
이때 절댓값이 같은 값에 대한 handling을 위해서 내림차순(절댓값은 같지만 양수값을 우선순위가 더 높게 처리)으로 구현하기 위해 -x 로 부여한다.


'''

def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), -x))
    
    return answer
