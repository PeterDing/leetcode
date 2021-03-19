from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    index = -1
    total = 0
    min_t = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        total += g - c
        if min_t > total:
            index = i
        min_t = min(min_t, total)

    if total < 0:
        return -1
    return index + 1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

index = canCompleteCircuit(gas, cost)
print(index)
