# 백준 1874
import sys

input = sys.stdin.readline

n = int(input())
A = [0] * n

for i in range(n):
    A[i]=(int(input()))

stack = []
num = 1 # 자동으로 증가하는 숫자
result = True
answer = ''

for i in range(n):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        n = stack.pop()
        if n > su:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'
if result:
    print(answer)

