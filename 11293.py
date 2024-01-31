import itertools

odd = ['1', '3', '5', '7', '9', 'B']


def check_num(num) -> bool:
    for i in range(1, len(num)):
        prev = num[i - 1]
        curr = num[i]
        if curr in odd and prev in odd:
            return False
    return True


numbers = '0123456789ABC'
comb = itertools.product(sorted(numbers), repeat=6)
counter = 0
for elem in comb:
    if elem[0] != '0' and elem.count('5') < 2 and check_num(elem):
        counter += 1
print(counter)
