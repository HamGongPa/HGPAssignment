# 1. 두 수의 합
def solution1(num1, num2):
    return num1 + num2


# 2. 두 수의 차
def solution2(num1, num2):
    return num1 - num2


# 3. 두 수의 곱
def solution3(num1, num2):
    return num1 * num2


#  4. 두 수의 나눗셈
def solution4(num1, num2):
    answer = int(num1/num2*1000)
    return answer


# 5. 몫 구하기
def solution5(num1, num2):  # 10 5 7 2
    a = num1//num2
    return a


# 6. 나머지 구하기
def solution6(num1, num2):
    answer = num1%num2
    return answer
