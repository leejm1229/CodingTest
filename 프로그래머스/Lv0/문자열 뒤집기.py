# 더 간결한 방식
def solution(my_string):
    return my_string[::-1]


my_string = 'jaron'
answer = ''
for i in range(len(my_string)-1,-1,-1):
    answer += my_string[i]
print(answer)