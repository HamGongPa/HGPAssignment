# 확인문제 2
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)


# 확인문제 3
limit = 10000
i = 1
sum_value = 0

while sum_value <= limit:
    sum_value += i
    i += 1

print(f"{i}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")


#확인문제 4
max_value = 0
a = 0
b = 0

for i in range(0, 100 // 2 + 1):
    j = 100 - i
    current = i * j
    if max_value < current:
        max_value = current
        a = i
        b = j
        
print(f"최대가 되는 경우: {a} * {b} = {max_value}")


# 배열 원소의 길이
def solution1(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


# 특정 문자 제거하기
def solution2(my_string, letter):
    return my_string.replace(letter, '')


# 자릿수 더하기
def solution3(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer



