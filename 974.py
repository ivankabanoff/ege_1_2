def get_r(num: int) -> int:
    bin_num = bin(num)[2:]
    for _ in range(2):
        if bin_num[-2] == bin_num[-1]:
            bin_num += '0'
        else:
            bin_num += '1'
    return int(bin_num, 2)


numbers = []
for n in range(3, 10000):
    if get_r(n) > 93:
        numbers.append(n)
print(min(numbers))