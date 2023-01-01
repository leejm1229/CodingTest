'''
2~3번째 줄: int()로 2진수 bin1과 bin2를 10진수로 바꾼다.
4번째 줄: 10진수로 바꾼 bin1과 bin2를 더해주고, 그 값을 bin()함수에 넣어 10진수 ➡️ 2진수로 만든다.
5번째 줄: 그대로 출력하게 되면 아래와 같은 화면처럼 2진수를 뜻하는 "0b"가 붙어서 나오기 때문에 문자열 슬라이싱을 이용하여 2번째부터 끝까지 출력한다.
'''
def solution(bin1, bin2):
    bin1, bin2 = int(bin1,2), int(bin2,2)
    answer = bin(bin1+bin2)
    return answer[2:]

'''
다른풀이
'''