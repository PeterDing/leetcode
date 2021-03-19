import math


def binary_search(target, ls, who):

    def bs(start, end):
        if start + 1 == end:
            return start
        mid = (start + end) // 2
        if target < ls[mid][who]:
            return bs(start, mid)
        else:
            return bs(mid, end)

    return bs(0, len(ls) - 1)


# A is the intervals
def merge(A, interval):
    if not A:
        return [interval]

    start, end = interval
    A.insert(0, [-math.inf, -math.inf])
    A.append([math.inf, math.inf])

    s = binary_search(start, A, 0)
    e = binary_search(end, A, 1) + 1

    r = []

    if A[s][1] < start:
        if A[s][0] != -math.inf:
            r.append(A[s])
    else:
        start = A[s][0]

    if A[e][0] > end:
        r.append([start, end])
        if A[e][0] != math.inf:
            r.append(A[e])
    else:
        end = A[e][1]
        r.append([start, end])

    return A[1:s] + r + A[e + 1:-1]


A = [[1, 5]]
interval = [2, 7]

ls = merge(A, interval)
print(ls)
