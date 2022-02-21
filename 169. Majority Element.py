class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a ={}
        
        for i in nums:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i]+=1
        
        max = -1
        res = -1
        for k,v in a.items():
            if v > max:
                max = v
                res = k
        return res