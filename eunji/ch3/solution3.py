# 1. 간단한 대화 프로그램

import datetime
now= datetime.datetime.now()

str_input=input("입력: ")

if str_input=="안녕" or str_input=="안녕하세요":
    print("안녕하세요!")
elif str_input=="지금 몇시야?" or str_input=="지금 몇시에요?":
    print(f"지금은 {now.hour}시입니다.")
else:
    print(str_input)



#2. 나누어 떨어지는 숫자

s_input=int(input("정수를 입력하세요>"))

if s_input%2==0:
    print(f"{s_input}은 2로 나누어 떨어지는 숫자입니다.")
else :
    print(f"{s_input}은 2로 나누어 떨어지는 숫자가 아닙니다.")



#3. 숫자 비교하기

def solution(num1, num2):
    if num1 == num2 :
        return 1
    else:
        return -1



#4. 옷가게 할인 받기

def solution(price):
    if 100000<=price<300000 :
        return(int(price*0.95))
    elif 300000<=price<500000 :
        return (int(price*0.90))
    elif 500000<=price<=1000000 :
        return(int(price*0.80))
    else :
        return(int(price))

