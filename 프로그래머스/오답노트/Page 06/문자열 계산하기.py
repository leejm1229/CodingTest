'''
my_string	result
"3 + 4"	    7
'''
def solution(my_string):
    arr = my_string.split(' ')
    
    answer = int(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            answer += int(arr[i+1])
        elif arr[i] == '-':
            answer -= int(arr[i+1])
    return answer

'''
eval함수란??
'eval(expression)' 으로 사용한다.

eval 함수는 한줄로 정리하자면 매개변수로 받은 expression(우리가 아는 일반적인 사칙연산 '식')을 문자열로 받아서, 실행하는 함수다. 
즉, 매개변수로 받은 expression은 파이썬에서 실행 가능한 문자열이 들어와야 한다는것이고, 
문자열로 들어온 그 expression을 파이썬이 실행해주는 함수이다.

그럼 식(expression)이란?

식은 값, 연산자, 변수 등 파이썬에서 사용하여 무언가를 표현할 수 있는 것을 말한다.

a > b 이런것도 식이고
1 + 2 이런것도 식이다.
'''

def solution(my_string):
    return eval(my_string)