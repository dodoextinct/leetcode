class Solution:
    def generate(self, k: int) -> List[List[int]]:
        
        r = [[1]]
        k -=1
        
        if k !=0:
            r.append([1,1])
            k-=1
        
        for i in range(k):
            t = r[i+1]
            l = []
            l.append(t[0])
            l+=[t[m]+t[m+1] for m in range(len(t)-1)]
            l.append(t[-1])
            r.append(l)
            
        return r
            