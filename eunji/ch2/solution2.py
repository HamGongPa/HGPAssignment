
#양꼬치
def solution1(n, k):
    answer = (12000*n+2000*k)-n//10*2000
    return answer

#특정 문자 제거하기
def solution2(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer

#문자열 뒤집기
def solution3(my_string):
    answer = my_string[::-1]
    return answer

#대문자로 변경
def num():
    input_z=input("문자열을 입력하세요 > ")
    print("원본: ", input_z)
    print("변환: ", input_z.upper())
