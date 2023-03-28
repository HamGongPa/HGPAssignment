# 1. 짝수는 싫어요
def solution1_1(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer

def solution1_2(n):
    return [i for i in range(1, n+1, 2)]

# 2. 짝수 홀수 개수
def solution2(num_list):
    answer = [0, 0]
    for num in num_list:
        answer[num % 2] += 1
    return answer

# 3. 아이스 아메리카노
def solution3(money):
    return divmod(money, 5500)

# 4. 편지
def solution4(message):
    return len(message) * 2

# 5. 369게임
def solution5(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))