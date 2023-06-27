# N보다 커질 때까지 더하기
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            return answer

# 원소들의 곱과 합
def solution(num_list):
    a = 1
    for i in num_list:
        a *= i
    if a < sum(num_list) ** 2:
        return 1
    else:
        return 0


# N개 간격의 원소들
def solution(num_list, n):
    return num_list[::n]

#4
def join_string(*args):
    value = ",".join(args)
    return value

#5
def sum_nums(*args):
    result = 0
    for i in args:
        result += i
    return result
