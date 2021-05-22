# 0025 - Reverse Nodes in k-Group
#
# Road:
# Recursion
# recurse(h1 -> h2 -> h3 -> ...)
#     == (h2 -> h1) -> recurse(h3 -> ...)
#
# Writing cost time 21min


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = head
        for _ in range(k):
            if not p:
                return head
            p = p.next

        h = head
        r = self.reverse(h, k)
        h.next = self.reverseKGroup(p, k)

        return r

    def reverse(self, head: ListNode, k: int) -> ListNode:
        r = ListNode()
        h = head
        while k:
            p = r.next
            r.next = h
            h = h.next
            r.next.next = p

            k -= 1

        return r.next
