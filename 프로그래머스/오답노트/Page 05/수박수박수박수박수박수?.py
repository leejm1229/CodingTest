'''
n	return
3	"수박수"
4	"수박수박"
'''
def solution(n):
    answer = ''
    for i in range(n):
        if i %2 ==0:
            answer += '수'
        else:
            answer += '박'
        
    return answer