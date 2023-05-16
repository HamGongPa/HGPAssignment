# 1. 도전문제1 : 숫자의 종류 (p.268)
def solution1():
    l = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
    counter = {}
    for i in l:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1
    print(f"{l}에서 사용된 숫자의 종류는 {len(counter)}개 입니다.")


# 2. 도전문제2 : 염기의 개수 (p.268)
def solution2():
    nucleos = input("염기 서열을 입력해주세요: ")

    counter = {
        "a" : 0,
        "t" : 0,
        "g" : 0,
        "c" : 0
    }
    for i in nucleos:
        counter[i] += 1
    for key, value in counter.items():
        print(f"{key}의 개수 : {value}")


# 3. 도전문제3 : 2차원 리스트 평탄화 (p.269)
def solution3():
    a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
    output = []

    for i in a:
        if type(i) is int:
            output.append(i)
        else:
            for j in i:
                output.append(j)
    print(output)


# 4. 문자열 정수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181849
def solution4(num_str):
    return sum(list(map(int, num_str)))


# 5. 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
from math import prod
def solution5(num_list):
    return 1 if prod(num_list) < sum(num_list) ** 2 else 0


# 6. 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120906
def solution6(n):
    return sum(list(map(int,str(n))))

# 7. 카운트 업
# https://school.programmers.co.kr/learn/courses/30/lessons/181920
def solution7(start, end):
    return [i for i in range(start, end+1)]