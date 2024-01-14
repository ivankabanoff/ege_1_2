def process(num: int) -> int:
    bin_num = bin(num)[2:]
    if len(bin_num) % 2:
        return int('1' + bin_num + '01', 2)
    return int(bin_num[:len(bin_num) // 2] + '000' + bin_num[len(bin_num) // 2:], 2)


n = 0
while process(n) <= 100:
    n += 1
print(n)


