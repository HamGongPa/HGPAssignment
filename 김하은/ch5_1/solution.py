문제#1
def solution1(numbers, n):
    answer = 0
    for i in numbers:
        if answer > n:
            return answer
        else:
            answer += i
    return answer


문제#2
def solution2(num_list):
    a = 1
    s = 0
    for i in num_list:
        a *= i
        s += i
    if sum(num_list) ** 2 > a:
        return 1
    else:
        return 0


문제#3
def solution3(num_list, n):
     return [(num_list[i]) for i in range(0, len(num_list), n)] 


문제#4
def join_string(*args):
    value = ",".join(args)
    return value

join_string('a','b','c','c')

문제#5
def sum_nums(*args):
    result = 0
    for arg in args:
        result += arg
    return result

sum_nums(10,20,30)
sum_nums(10,20,30,70,11)
