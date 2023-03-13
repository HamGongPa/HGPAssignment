#1. 간단한 대화 프로그램
import datetime
now = datetime.datetime.now()
s = input("입력:")
if s == "안녕" or s == "안녕하세요"
    print("안녕하세요")
elif s == "지금 몇 시야?" or "지금 몇 시예요?":
    print(f"지금은 {now.hour}시입니다.")
else:
    print(s)


#2. 나누어 떨어지는 숫자
n = input("정수를 입력해주세요.")
n = int(n)
if n % 2 == 0:
    print(f"{n}은 2로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{n}은 2로 나누어 떨어지는 숫자가 아닙니다.")


#3. 숫자 비교하기
def solution1(num1, num2):
    if num1==num2:
        return 1
    else:
        return -1


#4. 옷가게 할인받기
def solution2(price):
    if 500000 <= price:
        return int(price * 0.8)
    elif 300000 <= price:
        return int(price * 0.9)
    elif 100000 <= price:
        return int(price * 0.95)
    else:
        return int(price)