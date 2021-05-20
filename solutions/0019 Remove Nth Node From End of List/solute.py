# 0019 - Remove Nth Node From End of List
#
# Road:
#
# Writing cost time 19min


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = None
        p2 = head
        count = 1

        while p2.next:
            if count == n:
                if not p1:
                    p1 = head
                else:
                    p1 = p1.next
            else:
                count += 1

            p2 = p2.next

        if not p1:
            return head.next
        else:
            p1.next = p1.next.next
            return head
