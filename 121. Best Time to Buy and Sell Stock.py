class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        mi, ma = p[0], 0
        
        for i in range(0, len(p)):
            if mi > p[i] and i != len(p)-1:
                mi = p[i]
            else:
                ma = max(ma, p[i]-mi)
                
        return ma