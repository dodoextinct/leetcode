# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        a = ListNode()
        b = a
        p =None
        carry  = 0
        while l1 or l2:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0
            a.next = ListNode(((t1 + t2) + carry)%10)
            carry = ((t1 + t2) + carry)//10
            a = a.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry>0:
            a.next = ListNode(carry)
        return b.next  
            