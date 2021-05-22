# 0023 - Merge k Sorted Lists
#
# Road:
# Using heap for k head nodes
#
# Writing cost time 17min


import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        r = head

        min_heap = []

        for i, h in enumerate(lists):
            if h:
                heapq.heappush(min_heap, (h.val, i))

        while min_heap:
            _, i = heapq.heappop(min_heap)
            r.next = lists[i]

            # !!! To connect next node
            r = r.next

            lists[i] = lists[i].next

            h = lists[i]
            if h:
                heapq.heappush(min_heap, (h.val, i))

        return head.next
