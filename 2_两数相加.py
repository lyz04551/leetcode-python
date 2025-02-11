# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         res = ListNode(None)
#         result = res
#         b = 0
#         while l1 and l2:
#             sum_temp = l1.val + l2.val + b

#             a = sum_temp % 10
#             b = sum_temp // 10

#             res.next = ListNode(a)

#             l1 = l1.next
#             l2 = l2.next
#             res = res.next

#         return result.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


print(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))