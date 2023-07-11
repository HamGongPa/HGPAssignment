# 1. n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884
def solution1(numbers, n):
    sum = 0
    for number in numbers:
        sum += number
        if sum > n:
            return sum


# 2. 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
from math import prod
def solution2(num_list):
    return 1 if prod(num_list) < sum(num_list) ** 2 else 0


# 3. N개 간격의 원소들
# https://school.programmers.co.kr/learn/courses/30/lessons/181888
def solution3(num_list, n):
    return num_list[::n]


# 4. 빈칸 채우기
def join_string(*args):
    value = ','.join(args)
    return value


# 5. 빈칸 채우기
def sum_nums(*args):
    result = 0
    for arg in args:
      result += arg
    return result



