## 2 Ptrs
### Date: 08/15/2023

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                s2s=nums[i]+nums[j]
                ind = bisect.bisect_left(nums,s2s)
                ans += max(0,ind-j-1)
        return ans
