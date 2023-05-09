import datetime

# 1. 간단한 대화 프로그램
def solution1():
    now = datetime.datetime.now()
    s = input("입력: ")
    if s == "안녕" or s == "안녕하세요.":
        print("안녕하세요.")
    elif s =="지금 몇 시야?" or s == "지금 몇 시예요?" :
        print(f"지금은 {now.hour}시입니다.")
    else:
        print(s)
 
# 2. 나누어 떨어지는 숫자
def solution2():
    n = input("정수를 입력해주세요: ")
    if int(n) % 2 == 0 :
        print(f"{n}은 2로 나누어 떨어지는 숫자입니다.")
    else:
        print(f"{n}은 2로 나누어 떨어지는 숫자가 아닙니다.")

# 3. 숫자 비교하기
def solution3(num1, num2):
    return 1 if num1==num2 else -1

# 4. 옷가게 할인 받기
def solution4(price):
    answer = 0
    if price < 100000:
        answer = price 
    elif 100000 <= price <300000:
        answer = price * 0.95
    elif 300000 <= price < 500000:
        answer = price * 0.9
    elif 500000 <= price:
        answer = price * 0.8
    return int(answer)