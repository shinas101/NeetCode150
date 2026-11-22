class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        self.backtrack(nums,0)
        return self.res


    def backtrack(self,num,idx):
        if idx == len(num):
            self.res.append(num[:])
            return
        for i in range(idx,len(num)):
            num[idx] , num[i] = num[i] , num[idx]
            self.backtrack(num,idx+1)
            num[idx] , num[i] = num[i] , num[idx]

        
