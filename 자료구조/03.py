# 백준 11659
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum = [0]

for i in range(len(lst)):
    sum.append(sum[i]+lst[i])

for i in range(m):
    a,b = map(int, input().split())
    print(sum[b] - sum[a-1])
