문제 #1
key_list = [“name”, “hp”, “mp”, “level”]
value_list = [“기사”, 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
    
print(character)


문제#2
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i +=1

print(“{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.”.format(i-1, limit, sum_value))


문제#3
max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current
        
print("최대가 되는 경우: {} * {} ={}".format(a,b, max_value))


문제#4 
def solution1(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer


문제#5
def solution2(my_string, letter):
    answer = my_string.replace(letter,"")
    return answer


문제#6
def solution3(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
