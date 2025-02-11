# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        b = headB
        a = headA
        while True:
            if headA == headB:
                return headA
            else:
                headA = headA.next if headA else b
                headB = headB.next if headB else a
        return None
        # while a!=b:
        #     a = a.next if a else headB
        #     b = b.next if b else headA
        # return a
    

# print(Solution().getIntersectionNode(ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))Solution().getIntersectionNode(ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(2, ListNode(3))))))))

print(Solution().getIntersectionNode(ListNode(1, ListNode(2, ListNode(3))),ListNode(2)))
