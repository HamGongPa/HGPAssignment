# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
            answer.append(i)
    return answer

# 짝수 홀수 개수
def solution(num_list):
    a = []
    b = []
    for i in num_list:
        if i % 2 == 0:
            a.append(i)
        else: b.append(i)
    return [len(a), len(b)]

# 아이스 아메리카노
def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer

# 편지
def solution(message):
    return len(message) * 2

# 369게임
def solution(order):
    answer = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1
    return answer