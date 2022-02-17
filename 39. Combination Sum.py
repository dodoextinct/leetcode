class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths=[]
        length=len(candidates)

        def Helper(idx,currentPath,target):
            if target<0:
                return
            if target==0:
                paths.append(currentPath[:])
                return
            for i in range(idx,length):
                ele=candidates[i]
                currentPath.append(ele)
                Helper(i,currentPath,target-ele)
                currentPath.pop()

        Helper(0,[],target)  
        return paths