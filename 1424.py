def get_r(num: int) -> int:
    bin_num = bin(num)[2:]
    if int(bin_num) % 2:
        return int(bin_num + '10', 2)
    return int(bin_num + '01', 2)


n = 0
while get_r(n) <= 281:
    n += 1
print(n)