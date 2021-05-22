# 0024 - Swap Nodes in Pairs
#
# Road:
# Recursion:
# recurse(l -> r -> p -> ...)
#      == r -> l -> recurse(p -> ...)
#
# Writing cost time 8min


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head

        if not head.next:
            return head

        l = head
        r = head.next

        p = r.next

        r.next = l
        l.next = self.swapPairs(p)

        return r
