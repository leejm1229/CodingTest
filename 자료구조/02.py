# 백준 1546
import sys

input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
lst = []
max_num = max(tmp)

for i in tmp:
    lst.append(i/max_num*100)

print(sum(lst)/n)
