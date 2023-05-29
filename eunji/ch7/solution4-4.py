# 도전문제 1번
a = [1,2,4,3,2,1,2,1,2,1,2,1]
count = {}

for A in a:
    if A not in count:
        count[A] = 0
    count[A] += 1
    
print(f"{a}에서 사용된 숫자의 종류는 {len(count)}개 입니다.")
print(f"참고: {count}")





# 도전문제 2번
a = input("염기 서열을 입력해주세요: ")
count = {}

for A in a:
    if A not in count:
        count[A] = 0
    count[A] += 1
for key, element in count.items():
    print(f"{key}의 개수: {element}")





# 도전문제 4번
a = [1,2,[3,4],5,[6,7],[8,9]]
b = []

for i in a:
    if type(i) == list:
        for j in i:
            b.append(j)
    else:
        b.append(i)

print(f"{a}를 평탄화하면 {b}입니다.")





# 문자열 정수의 합
def solution(num_str):
    sum = 0
    for i in num_str:
        sum += int(i)
    return sum





# 원소들의 곱과 합

def solution(num_list):
    mul = 1
    plus = 0

    for i in num_list:
        mul *= i
        plus += i
    if mul < plus * plus: 
        return 1
    else: 
        return 0





# 자릿수 더하기

def solution(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum





# 카운트 업
def solution(start, end):
    answer = []
    for i in range(start, end + 1):
        answer.append(i)
    return answer
