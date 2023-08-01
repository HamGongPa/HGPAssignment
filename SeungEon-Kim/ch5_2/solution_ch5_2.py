# 1. Quiz 1
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]

def flatten(data):
    output = []
    for i in data:
        if type(i) == list:
            output += flatten(i)
        else:
            output.append(i)
    return output


# 2. Quiz 2
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)


# 3. Quiz 3
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)