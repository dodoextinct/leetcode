# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        f,s = head, head
        
        while f and f.next:
            
            f = f.next.next
            s = s.next
            
        return s
            