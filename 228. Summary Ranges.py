class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        nums+=[22]
        st = nums[0]
        
        r = []
        
        for i in range(1,len(nums)):
            if nums[i] != 1+nums[i-1]:
                if st != nums[i-1]:
                    r.append("{}->{}".format(st, nums[i-1]))
                else:
                    r.append(str(st))
                st = nums[i]
        
        return r