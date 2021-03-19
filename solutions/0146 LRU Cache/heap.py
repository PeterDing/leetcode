def heappush(heap, item):
    heap.append(item)

    if not heap:
        return heap

    def sort(heap, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        if heap[parent_index] > heap[index]:
            heap[parent_index], heap[index] = heap[index], heap[parent_index]
            sort(heap, parent_index)

    index = len(heap) - 1
    sort(heap, index)


def heappop(heap, index=None):
    poped = heap[0]

    tail = heap.pop()
    if not heap:
        return tail

    heap[0] = tail

    def sort(heap, index):
        left = 2 * index + 1
        left_item = None
        if left < len(heap):
            left_item = heap[left]

        right = left + 1
        right_item = None
        if right < len(heap):
            right_item = heap[right]

        item = heap[index]
        if left_item and left_item < item:
            heap[left], heap[index] = heap[index], heap[left]
            item = left_item
            sort(heap, left)

        if right_item and right_item < item:
            heap[right], heap[index] = heap[index], heap[right]
            sort(heap, right)

    sort(heap, 0)
    return poped


def heapify(array):
    heap = []
    for item in array:
        heappush(heap, item)

    return heap


v = list(range(10, 0, -1))

v = heapify(v)
print(v)

heappush(v, 3.3)
heappush(v, 5.6)
heappush(v, 100)

print(v)

while v:
    print(heappop(v))
