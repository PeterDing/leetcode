import math

def search(n, pers=0.000000000000001):
    start = 0
    end = n
    while True:
        m = (end + start) / 2

        if abs(n - m**2) < pers:
            return m

        if m**2 < n:
            start = m
        else:
            end = m



n = 41
print(search(n))
print(math.sqrt(n))
