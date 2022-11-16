'''
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
'''




# 형 변환 후 조인 함수 이용
def solution(phone_number):
    arr = list(phone_number)
    for i in range(len(arr)-4):
        arr[i] = '*'
    
    return ''.join(i for i in arr)

def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]