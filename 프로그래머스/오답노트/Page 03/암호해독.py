'''
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
'''

'''
a[start : end : step]
start: 슬라이싱을 시작할 시작위치입니다.
end: 슬라이싱을 끝낼 위치로 end는 포함하지 않습니다!
step: stride(보폭)라고도 하며 몇개씩 끊어서 가져올지와 방향을 정합니다. 옵션이며 아래의 예제를 확인하면 쉽게 이해가 가능합니다.
'''
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer