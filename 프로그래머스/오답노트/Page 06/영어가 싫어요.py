'''
numbers	                                    result
"onetwothreefourfivesixseveneightnine"	    123456789
"onefourzerosixseven"	                    14067
'''
# replace 함수는 원소가 다 str 타입이어야 한다.
def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    
    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))
        
    return int(numbers)