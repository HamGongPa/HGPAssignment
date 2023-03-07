# 1. 양꼬치
def solution1(n, k):
    return 12000 * n + 2000 * (k - n // 10)


# 2. 특정 문자 제거
def solution2(my_string, letter):
    return my_string.replace(letter, '')


# 3. 문자열 뒤집기
def solution3(my_string):
    return my_string[::-1]


# 4. 문자열을 입력받아 대문자로 변환
def solution4():
    my_string = input("문자열을 입력하세요>")
    print("원본:", my_string)
    print("변환:", my_string.upper())


