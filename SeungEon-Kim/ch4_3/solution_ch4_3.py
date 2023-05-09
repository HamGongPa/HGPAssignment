# 1. 확인문제 2
def solution1():
    key_list = ["name", "hp", "mp", "level"]
    value_list = ["기사", 200, 30, 5]

    character = {}
    for i in range(len(key_list)):
        character[key_list[i]] = value_list[i]
    
    print(character)

# 2. 확인문제 3
def solution2():
    limit = 10000
    i = 1
    sum_value = 0

    while sum_value < limit:
        sum_value += i
        i+=1

    print(f"{i}를 더할 때 {limit}을 넘으며 그 때의 값은 {sum_value}입니다.")

# 3. 확인문제 4
def solution3():
    max_value = 0
    a = 0
    b = 0
    for i in range(1, 100//2 + 1):
        j = 100 - i

        current = i  * j
        if max_value < current:
            a = i
            b = j
            max_value = current

    print(f"최대가 되는 경우: {a} * {b} = {max_value}")

# 4. 배열 원소의 길이
def solution4(strlist):
    answer = []
    for s in strlist:
        answer.append(len(s))
    return answer

# 5. 특정 문자 제거하기
def solution5(my_string, letter):
    return my_string.replace(letter,'')

# 6. 자릿수 더하기
def solution6(n):
    return sum(list(map(int,str(n))))
