class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()

        def backtrack(subset,idx):
            if idx == len(nums):
                res.add(tuple(subset))
                return
            
            subset.append(nums[idx])
            backtrack(subset, idx + 1)
            subset.pop()
            backtrack(subset, idx + 1)
        backtrack([],0)
        return [list(s) for s in res]

        
