# 1. 도전문제(숫자의 종류)
def solution1
    1 = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
    counter = {}

    for j in i:
        if j in counter:
            counter[j] += 1
        else:
            counter[j] = 1

    print(counter)
    {1: 4, 2: 3, 3: 3, 4:2}
    len(counter)
    4
    print(f"{1}에서 사용된 숫자의 종류는 {len(counter)}개입니다.")
    [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]에서 사용된 숫자의 종류는 4개입니다.


#2. 도전문제(염기의 개수)
def solution2
    nucleos = input("염기 서열을 입력해주세요: ")
    염기 서열을 입력해주세요 : catgacgataaacgttggtgacaacc

    counter = {
        "a": 0,
        "t": 0,
        "g": 0,
        "c": 0,
    }

    for i in counter.items():
        print(f"{i}의 개수: {value}")

        ('a', 1)의 개수: 값c
        ('t', 11)의 개수 : 값c
        ('g', 2)의 개수: 값c
        ('c', 5)의 개수: 값c
    for key, value in counter.items():
        print(f"{key}의 개수: {value}")

    a의 개수:1
    t의 개수:11
    g의 개수:2
    c의 개수:5



#3. 도전문제(2차원 리스트 평탄화)
def solution3
    a = [1, 2, [3,4], 5, [6, 7], [8, 9]]
    output = []

    for i in a:
        print(i)
    1
    2
    [3, 4]
    5
    [6, 7]
    [8, 9]

    for i in a:
        if type(i) == list:
            for j in i:
                output.append(j)
        else:
            output.append(i)

    output
    [1, 2, 3, 4, 5, 6, 7, 8, 9]


#4. 문자열 정수의 합
def solution4(num_str):
    answer = 0
    num_str = int(num_str)
    while num_str>0:
        answer += num_str%10
        num_str //= 10
    return answer


#5. 원소들의 곱과 합
def solution5(num_list):
    answer = 0

    if sum(num_list) ** 2 > num_list:

    r


#6. 자릿수 더하기
 def solution6(n):
        answer = 0
        while n != 0:
            answer += n % 10
            n = n // 10

        return answer


 #7. 카운트 업
def solution7(start, end):
    answer = [num for num in range(start, end + 1)]
    return answer