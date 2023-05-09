# 1. 키와 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리로 만들기

key_list = ['name', 'hp', 'mp', 'level']
value_list = ['기사', 200, 30, 5]
character = {}

for i in range(0, 4):
    character[key_list[i]] = value_list[i]
    
print(character)





# 2. 1부터 숫자를 증가시키면서 몇을 더할 때 1000이 넘는지 구하라

limit = 1000
i = 1

sum_value = 0
while sum_value <= limit:
    sum_value += i
    i += 1

print(f"{i}를 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")





# 3. 1~100을 (1*99, 2*98, 3*97 ...) 다음과 같이 계산한다고 할 때, 최대가 되는 경우

max_value = 0
a = 0
b = 0

for i in range (0, 99+1):
    j = 100 - i
    
    if max_value < i * j:
        a = i
        b = j
        max_value = i * j

print(f"최대가 되는 경우: {a} * {b} = {max_value}")





# 4. 배열 원소의 길이 구하기

def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer





# 5. 특정 문자 제거하기

def solution(my_string, letter):
    answer = my_string.replace(letter,'')
    return answer





# 6. 자릿수 더하기

def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)
        
    return answer
