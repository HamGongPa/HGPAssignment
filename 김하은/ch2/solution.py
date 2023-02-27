양꼬치 (2주차 문제풀이)
def solution1(n, k):
    answer = n*12000 + k*2000 - (n//10)*2000
    return answer

특정 문자 제거하기
def solution2(my_string, letter):
    answer = my_string.replace(letter,"")
    return answer

문자열 뒤집기
def solution3(my_string):
    answer = my_string[::-1]
    return answer

문자열 대문자로 변환
def solution4():
    my_string = input("문자열을 입력하세요>")
    print("원본:",my_string)
    print("변환:",my_string.upper())

