import itertools

alp = 'гондубш'
comb = itertools.product(sorted(alp), repeat=6)
ans = 0
for num, elem in enumerate(comb, 1):
    if num % 2 and elem[0] != 'б' and elem.count('н') >= 2 and 'у' not in elem:
        ans = num
print(ans)