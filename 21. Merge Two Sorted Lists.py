# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l = []
        def merge(n1, n2):
            if not n1:
                while n2:
                    l.append(n2.val)
                    n2 = n2.next
            elif not n2:
                while n1:
                    l.append(n1.val)
                    n1 = n1.next
            else:
                if n1.val <= n2.val:
                    l.append(n1.val)
                    merge(n1.next, n2)
                else:
                    l.append(n2.val)
                    merge(n1, n2.next)

        merge(l1,l2)        
        r = a = ListNode(0)
        
        for i in l:
            a.next =  ListNode(i)
            a = a.next
            
        return r.next
        
                
            