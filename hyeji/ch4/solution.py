# 1. 짝수는 싫어요
def solution1(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
            answer.append(i)
    return answer


# 2. 짝수 홀수 개수
def solution2(num_list):
    answer = [0, 0]

    for i in num_list:
        answer[i % 2] += 1

    return amswer


# 3. 아이스 아메리카노
def solution3(money):
    return [money // 5500, money % 5500]


# 4. 편지
def solution4(message):
    return len(message)*2


# 5. 369게임
def solution5(order):
    answer = 0
    while order:
        if order % 10 in [3, 6, 9]:
            answer += 1
        order //= 10
    return answer
