from collections import defaultdict


def str_it(num, de):
    d = defaultdict(int)
    ss = []

    sign = -1 if num * de < 0 else 1
    if sign == -1:
        ss.append('-')

    num = abs(num)
    de = abs(de)

    t = num // de
    ss.append(str(t))
    if num % de == 0:
        return ''.join(ss)
    else:
        ss.append('.')

    zeros = 0
    mod = num % de
    while True:
        if mod == 0:
            return ''.join(ss)

        if mod < de:
            mod *= 10
            zeros += 1
            continue

        ss.append('0' * (zeros - 1))
        zeros = 0

        if mod in d:
            i = d[mod]
            return ''.join(ss[:i]) + '(' + ''.join(ss[i:]) + ')'

        d[mod] = len(ss)

        t = mod // de
        ss.append(str(t))

        mod = mod % de


print(str_it(7, 13))
print(str_it(1, 2))
print(str_it(13, 6))
print(str_it(1, 10953))
print(str_it(-50, 8))
