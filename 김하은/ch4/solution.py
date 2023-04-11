#짝수는 싫어요
def solution1(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            print(i)
            answer.append(i)
    return answer

#짝수 홀수 개수
def solution2(num_list):
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b +=1
    answer=[a,b]
    return answer

#아이스 아메리카노
def solution3(money):
    answer = [money//5500,money%5500]
    return answer

#편지
def solution4(message):
    answer = len(message)*2
    return answer

#369게임
def solution5(order):
    answer = str(order).count("3") + str(order).count("6") + str(order).count("9")
    return answer
