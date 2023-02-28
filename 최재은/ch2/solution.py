#양꼬치
def solution1(n,k):
    return 12000 * n + 2000 * k - n//10 * 2000

#특정 문자 제거하기
def solution2(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer

#문자열 뒤집기
def solution3(my_string):
    reverse = my_string[::-1]
    return reverse

#문자열을 입력받아 대문자로 변환하기
def solution4():
    a = input("문자열을 입력하세요>")
    print("원본:", a)
    print("변환:", a.upper())


