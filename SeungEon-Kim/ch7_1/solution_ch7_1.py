# 1. 랜덤 실수(0 ~ 1 사이)를 생성하여 반올림하는 함수 (랜덤, 수학 관련 모듈)
import random

def round_random():
    ran = random.random()
    print(f"a : ", ran)
    print(f"b : ", round(ran))

round_random()


# 2. 생일 파라미터로 입력, 무슨 요일인지 출력하는 함수 (요일 찾는 함수)
import datetime

def birth(year, month, day):
    birthday = datetime.date(year, month, day).weekday()
    return birthday

birth(1998, 11, 27)