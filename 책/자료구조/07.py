# 백준 1940
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

lst = list(map(int, input().split()))
count = 0
i = 0
j = N - 1
lst.sort()

while i < j:
    if lst[i] + lst[j] < M:
        i += 1
    elif lst[i] + lst[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
