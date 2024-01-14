def get_r(num: int) -> int:
    num -= num % 4
    bin_n = bin(num)[2:]
    for _ in range(2):
        bin_n = bin_n + str(sum([int(x) for x in bin_n]) % 2)
    return int(bin_n, 2)


numbers = []
for n in range(100000):
    if get_r(n) < 64:
        numbers.append(n)
print(max(numbers))