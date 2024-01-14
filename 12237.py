def process(num: int) -> int:
    bin_num = bin(num)[2:]
    if num % 2:
        res = '1' + bin_num + '0'
    else:
        res = bin_num + bin_num[-2:]
    res = int(res, 2)
    return res


numbers = []
for n in range(10000):
    if process(n) < 100:
        numbers.append(n)
print(f'Максимальное n: {max(numbers)}')
