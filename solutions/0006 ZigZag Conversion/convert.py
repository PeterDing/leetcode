def convert(s: str, numRows: int) -> str:
    if len(s) < 2 or numRows == 1:
        return s

    a = range(numRows - 1)
    b = range(numRows - 1, 0, -1)

    iters = list(a) + list(b)

    rs = [''] * numRows
    for i, e in enumerate(s):
        p = i % len(iters)
        rs[iters[p]] += e

    return ''.join(rs)


print(convert('abcdef', 3))
