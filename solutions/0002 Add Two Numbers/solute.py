# 0002 - Add Two Numbers
#
# Road:
# Skipping
#
# Writing cost time 10min

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        r = root

        remain = 0
        while l1 or l2:
            n1 = 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            n2 = 0
            if l2:
                n2 = l2.val
                l2 = l2.next

            s = n1 + n2 + remain
            val = s % 10
            remain = s // 10

            node = ListNode(val)
            r.next = node
            r = node

        if remain:
            node = ListNode(remain)
            r.next = node
            r = node

        return root.next
