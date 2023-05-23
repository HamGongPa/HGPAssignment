#도전문제: 숫자의 종류
l = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}

for i in l:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

print(f"{l}에서 사용된 숫자의 종류는 {len(counter)}개입니다.")


#도전문제: 염기의 개수
nucleos = input("염기 서열을 입력해주세요:")
염기 서열을 입력해주세요:gatcagtccaagttgac

counter = {
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0,
}
for i in nucleos:
    if i in counter:
        counter[i] += 1
for key, value in counter.items():
    print(f"{key}의 개수: {value}")


#도전문제: 2차원 리스트 평탄화
a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        for j in i:
            output.append(j)
    else:
        output.append(i)
        
print(output)
    

#문자열 정수의 합
def solution1(num_str):
    answer = 0
    for i in num_str:
        answer += int(i)
    return answer


#원소들의 곱과 합
def solution2(num_list):
    a = 1
    for i in num_list:
        a *= i
    if a < sum(num_list) ** 2:
        return 1
    else:
        return 0


#자릿수 더하기
def solution3(n):
    answer = 0
    a = str(n)
    for i in a:
        answer += int(i)
    return answer


#카운트 업
def solution4(start, end):
    answer = []
    for i in range(start, end+1):
        answer.append(i)
    return answer