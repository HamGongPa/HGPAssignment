# 1. 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1,n+1):
        if i % 2 != 0 :
            answer.append(i)
    return answer


# 2. 짝수 홀수 개수
def solution(num_list):
    z = []
    h = []
    
    for i in num_list:
        if i % 2 == 0:
            z.append(i)
        else :
            h.append(i)
            
        answer = [len(z),len(h)]
    return answer


# 3. 아이스 아메리카노
def solution(money):
    answer = []
    ia = 5500
    a = money // ia
    b = money % ia
    answer.insert(0,a)
    answer.insert(1,b)
    return answer


# 4. 편지
def solution(message):
    answer = len(message) * 2
    return answer


# 5. 369게임
def solution(order):
    clap = []
    for i in str(order):
        if i in ['3','6','9']:
            clap.append(i)
        answer = len(clap)
    return answer
