'''
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

n	    result
45	    7
125	    229

divmod() : 몫과 나머지를 리턴합니다. 리턴 값이 2개이므로 튜플을 사용합니다.
int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
'''
def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	
        answer += str(re)
    return int(answer, 3)

