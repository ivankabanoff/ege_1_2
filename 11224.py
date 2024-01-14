def to_3(num: int) -> str:
    res = ''
    while num != 0:
        res += str(num % 3)
        num //= 3
    return res[-1::-1]


def get_r(num: int) -> int:
    num = to_3(num)
    remainder = sum([int(x) for x in num]) % 4
    if remainder:
        num += to_3(remainder * 3)
    else:
        num = '1' + num[:-2]
    return int(num, 3)


numbers = []
n = 0
for n in range(1, 10000):
    if get_r(n) > 353:
        numbers.append(get_r(n))
print(min(numbers))
