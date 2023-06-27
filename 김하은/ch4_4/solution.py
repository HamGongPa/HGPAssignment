문제#1
num = [1,2,3,4,1,2,3,1,4,1,2,3]
counter = {}

for i in num:
    if i not in counter:
        counter[i] = 0
    counter[i] += 1

print(f"{num}에서")
print(f"사용된 숫자의 종류는 {len(counter)}입니다")
print(f"참고:{counter}")


문제#2
nucleos = input("염기 서열을 입력해주세요: ")
counter = {
    "a":0,
    "t":0,
    "g":0,
    "c":0,
    }

for i in nucleos:
    counter[i] += 1

print(counter)

for key, value in counter.items():
    print(f"{key}의 개수: {value}")


문제#3
num = [1,2,[3,4],5,[6,7],[8,9]]
output = []

for i in num:
    if type(i) == list:
        for j in i:
            output.append(j)
        else:
            output.append(i)

print(f"{num}를 평탄화하면")
print(f"{output}입니다")


문제#4
def solution4(num_str):
    answer = 0
    for i in str(num_str):
        answer += int(i)
    return answer


문제#5
def solution5(num_list):
    a = 1
    s = 0
    for i in num_list:
        a *= i
        s += i
    if sum(num_list) ** 2 > a:
        return 1
    else:
        return 0


문제#6
def solution6(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


문제#7
def solution7(start, end):
    answer = []
    for i in range(start, end+1):
        answer.append(i)
    return answer
