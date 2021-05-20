# 0021 - Merge Two Sorted Lists
#
# Road:
# two point
#
# Writing cost time 5min

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        r = head

        while l1 or l2:
            if not l1 and l2:
                r.next = l2
                break
            if l1 and not l2:
                r.next = l1
                break

            if l1.val < l2.val:
                r.next = l1
                l1 = l1.next
            else:
                r.next = l2
                l2 = l2.next

            r = r.next

        return head.next
