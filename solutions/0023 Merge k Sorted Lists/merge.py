# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Root:

    def __init__(self, ls: ListNode):
        self.p = ls

    def pop(self):
        if self.p.next:
            self.p = self.p.next

    def __lt__(self, root):
        return self.p.val < root.p.val


def mergeKLists(lists):
    r = ListNode(None)
    root = r

    heap = [Root(ls) for ls in lists if ls]
    heapq.heapify(heap)
    while heap:
        top = heapq.heappop(heap)
        root.next = top.p
        root = top.p
        if top.p.next:
            top.pop()
            heapq.heappush(heap, top)
    return r.next


def make_list(l):
    r = ListNode(None)
    root = r
    for x in l:
        root.next = ListNode(x)
        root = root.next
    return r.next


lists = [make_list(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
r = mergeKLists(lists)
s = []
while True:
    s.append(r.val)
    if not r.next:
        break
    r = r.next
