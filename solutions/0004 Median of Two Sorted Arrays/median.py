def median_true(l, start, end):
    mid = (start + end) // 2
    if (end - start) % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]


# A: --------------
#     left   | right
#            i
#
# B: -------------------
#    left  |  right
#          j
#
# i, j is the numbers of elements of left parts
# i + j = (m + n + 1) // 2
#
# These elements of left parts are always smaller than right parts'


def median(A, B):
    if len(A) > len(B):
        A, B = B, A

    m, n = len(A), len(B)

    imin, imax, haf = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = haf - i
        if A[i - 1] > B[j]:
            imax = i
        elif B[j - 1] > A[i]:
            imin = i
        else:
            la = 0
            if i != 0:
                la = A[i - 1]
            lb = B[j - 1]

            ra = 0
            if i != m:
                ra = A[i]
            rb = B[j]

            print(i, j, '--', la, lb, ra, rb)

            if (m + n) % 2 == 0:
                return (max(la, lb) + min(ra, rb)) / 2
            else:
                return max(la, lb)


def main():
    A = sorted([2, 4, 45, 63, 2, 46, 2, 12, 53, 56, 5, 542, 3, 1, 322, 534, 4])
    B = sorted([4.2, 534, 2, 32, 4, 6, 7, 8, 888, 7, 3, 424, 23, 5, 3, 9, 7, 6])

    # A = [1, 4, 9, 12, 13]
    # B = [5, 6, 7]

    m = median(A, B)
    print(m)

    L = sorted(A + B)
    print(median_true(L, 0, len(L)))


if __name__ == '__main__':
    main()
