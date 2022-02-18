class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        l = []
        
        for n in num:
            while l and k and l[-1]>n:
                l.pop()
                k -=1
                
            if l or n is not '0':
                l.append(n)
                
        if k:
            l = l[0:-k]
            
        return ''.join(l) or '0'