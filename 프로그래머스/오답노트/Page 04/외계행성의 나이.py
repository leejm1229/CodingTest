'''
a는 0 ~ j는 9
age	result
23	"cd"
51	"fb"
100	"baa"
소문자 a 아스키 코드 : 97
''' 

def solution(age):    
    return ''.join([chr(int(i)+97) for i in str(age)])