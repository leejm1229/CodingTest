# 백준 17298
n = int(input())
lst = []
flag = True
num = 1
lst = list(map(int, input().split()))

for i in range(n):
    cur = lst[i]
    while i+num != n:
        if cur < lst[i+num]:
            print(lst[i+num])
            break
        else:
            num += 1
    else:
        print(-1)
        break
    num = 1
    flag = True
