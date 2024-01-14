def get_r(num: int) -> int:
    bin_num = bin(num)[2:]
    for _ in range(2):
        bin_num = bin_num + str(sum([int(x) for x in bin_num]) % 2)
    return int(bin_num, 2)


n = 0
while get_r(n) <= 396:
    n += 1
print(get_r(n))

