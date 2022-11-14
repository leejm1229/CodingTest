# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return

import math
def solution(n):
    if math.sqrt(n) % 1 == 0:
        return 1
    else:
        return 2



def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2