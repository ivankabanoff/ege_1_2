def get_r(num: int) -> int:
    bin_num = bin(num)[2:]
    if not num % 2:
        bin_num += bin_num[-2:]
    else:
        bin_num = '1' + bin_num + '1'
    return int(bin_num, 2)


numbers = []
for n in range(10000):
    if get_r(n) > 130:
        numbers.append(get_r(n))
print(min(numbers))

