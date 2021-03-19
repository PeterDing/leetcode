def gen_pares(l, r, stock, rs):
    if l == 0 and r == 0:
        rs.append(''.join(stock))

    # Here, we have two selections to do
    # 1. add a (
    if l > 0 and l <= r:
        stock.append('(')
        gen_pares(l - 1, r, stock, rs)
        stock.pop()

    # 2. add a )
    if r > 0:
        stock.append(')')
        gen_pares(l, r - 1, stock, rs)
        stock.pop()


n = 4
rs = []
gen_pares(n, n, [], rs)

for i in rs:
    print(i)
