# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        if not head.next and n == 1:
            return None
        a = head
        c = 0
        while a.next:
            c+=1
            a = a.next
        a = head
        while (c-n > 0):
            a=a.next
            c-=1
            
        if a == head and c != n:
            head = a.next
        else:
            a.next = a.next.next if a.next.next !=None else None
        
        return head