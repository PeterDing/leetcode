def candy_sum(ratings):
    N = len(ratings)

    candys = [0] * N

    for i in range(N - 1):
        a = ratings[i]
        b = ratings[i + 1]

        if a < b:
            candys[i + 1] = candys[i] + 1

    for i in range(N - 1, 0, -1):
        a = ratings[i]
        b = ratings[i - 1]

        if b > a:
            candys[i - 1] = max(candys[i - 1], (candys[i] + 1))

    return sum(candys) + N




class Solution:
    def candy(self, ratings: List[int]) -> int:
        return candy_sum(ratings)
