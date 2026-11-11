class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        ans = []
        for key, v in nums.items():
            heappush(ans, (v, key))
            if len(ans)>k:
                heappop(ans)
        return [key for v, key in ans]        
