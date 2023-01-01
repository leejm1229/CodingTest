'''
my_str	                n	        result
"abc1Addfggg4556b"	    6	        ["abc1Ad", "dfggg4", "556b"]
"abcdef123"	            3	        ["abc", "def", "123"]
'''
# ange함수 매개변수에 숫자를 세개 넣는 경우 
# range(A, B, C)
# A부터 C 숫자만큼의 간격으로 B-1 까지의 정수 범위를 반환합니다. B까지가 아닌 B-1 이라는 것에 주의하세요.
for i in range(1, 7 ,2):
    print(i) # 1, 3, 5

def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]