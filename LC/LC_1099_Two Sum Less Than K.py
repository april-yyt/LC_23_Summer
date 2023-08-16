## 2 Ptrs
### Date: 08/15/2023

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        lo,hi = 0, len(nums)-1
        sum = -1
        while lo < hi:
            if nums[lo] + nums[hi] < k:
                sum = max(sum, nums[lo]+nums[hi])
                lo += 1
            else:
                hi -= 1
        return sum
