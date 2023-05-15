# 1. 확인문제2
def solution1
    key_list = ["name", "hp", "mp", "level"]
    value_list = ["기사", 200, 30, 5]
    character = {}
    for i in range(len(key_list)):
        character[key_list[i]] = value_list[i]

        character
        {'name': '기사', 'hp': 200, 'mp': 30, 'level': 5}


# 2. 확인문제3
def solution2
    limit = 10000
    i = 1
    sum_value = 0

    while sum_value < 10000:
        sum_value += i
        i += 1
        print(sum_value, i)


        sum_value
        10011


# 3. 확인문제4
def solution3
    max_value = 0
    a = 0
    b = 0
    for i in range(1, 100 // 2+1):
        j = 100 - i
        if max_value= i*(100-i)
            a = i
            b = j
            print(max_value) = i


# 4. 배열 원소의 길이
def solution4(strlist):
        return [len(word) for word in strlist]


# 5. 특정 문자 제거하기
def solution5(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i

    return answer


# 6. 자릿수 더하기

def solution6(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n = n // 10

    return answer