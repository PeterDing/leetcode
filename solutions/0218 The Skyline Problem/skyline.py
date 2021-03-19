import heapq


def reduce_rs(rs):
    while len(rs) > 1:
        item = rs.pop()
        if rs[-1][0] == item[0]:  # equal coo
            rs[-1][1] = max(rs[-1][1], item[1])
        else:
            if rs[-1][1] != item[1]:  # equal high
                rs.append(item)
            break


def append_rs(rs, item):
    rs.append(item)
    reduce_rs(rs)
    return

    if rs:
        print('--', rs[-1], item)
        if rs[-1][0] == item[0]:  # equal coo
            rs[-1][1] = max(rs[-1][1], item[1])
        else:
            if rs[-1][1] != item[1]:  # equal high
                rs.append(item)
    else:
        rs.append(item)

    reduce_rs(rs)


def skyline(buildings):
    if not buildings:
        return []

    minHeap = []  # store (right corrdinates, high)
    maxHeap = []  # store (-high, right corrdinates)

    rs = []

    for left, right, high in buildings:
        while minHeap and left >= minHeap[0][0]:
            pre_right, pre_high = heapq.heappop(minHeap)
            if pre_high == -maxHeap[0][0]:
                heapq.heappop(maxHeap)
                if not maxHeap:
                    append_rs(rs, [pre_right, 0])
                else:
                    while maxHeap:
                        next_h, next_right = maxHeap[0]
                        if pre_right < next_right:
                            append_rs(rs, [pre_right, -next_h])
                            break
                        heapq.heappop(maxHeap)
                    if not maxHeap:
                        append_rs(rs, [pre_right, 0])

        heapq.heappush(maxHeap, (-high, right))
        if high == -maxHeap[0][0]:
            append_rs(rs, [left, high])
        heapq.heappush(minHeap, [right, high])

    # print(minHeap)
    while minHeap:
        pre_right, pre_high = heapq.heappop(minHeap)
        if not maxHeap:
            append_rs(rs, [pre_right, 0])
            break

        if pre_high == -maxHeap[0][0]:
            heapq.heappop(maxHeap)
            if not maxHeap:
                append_rs(rs, [pre_right, 0])
            else:
                while maxHeap:
                    next_h, next_right = maxHeap[0]
                    if pre_right < next_right:
                        append_rs(rs, [pre_right, -next_h])
                        break
                    heapq.heappop(maxHeap)
                if not maxHeap:
                    append_rs(rs, [pre_right, 0])

    rs[-1][1] = 0

    return rs


buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
buildings = [[1, 5, 3], [1, 5, 3], [1, 5, 3]]
# buildings = [[0, 2, 3], [2, 5, 3]]
# buildings = [[2, 9, 10], [9, 12, 15]]
# buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
# buildings = [[0, 3, 3], [1, 5, 3], [2, 4, 3], [3, 7, 3]]
# from aa import bb as buildings
print(skyline(buildings))
print([[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
