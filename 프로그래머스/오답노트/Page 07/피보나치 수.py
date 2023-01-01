'''
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
n	return
3	2
5	5

'''
def solution(n):
    answer = [0,1]
    
    for i in range(2, n+1):
        answer.append((answer[i-2]+answer[i-1])%1234567)
    
    return answer[-1]