# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
              
        
        q = []
        q.append((0,root))
        
        a = 0
        while q:
            l = len(q)
            
                            
            n = []
            for i in range(l):
                id, node = q.pop(0)

                n.append(id)
                if node.left:
                    q.append((2*id+1, node.left))
                if node.right:
                    q.append((2*id+2, node.right))
                             
            a = max(a, max(n)-min(n)+1)
        return a