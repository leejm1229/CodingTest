# 백준 2018
import sys 

input = sys.stdin.readline

n = int(input())
sum = 1
count = 1
start = 1
end = 1
lst = []

while end != n :
    if sum == n :
        count += 1
        end += 1
        sum += end
    
    elif sum > n:
        sum -= start
        start += 1

    else:
        end += 1
        sum += end

print(count)
        
