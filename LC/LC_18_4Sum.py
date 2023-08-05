## Array

### Date: 07/17/2023

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSumTarget(nums, 4, 0, target)

    def nSumTarget( self, nums: List[int], n: int, start: int, target: int) -> List[List[int]]:
        res = []
        if n < 2 or len(nums) < n:
            return res
        if n == 2:
            # 2 ptrs
            lo, hi = start, len(nums)-1
            while lo < hi:
                s = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if s < target:
                    # make sure theres no duplicates
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif s > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
        else:
            # when n > 2, recursively calculate (n-1)sum
            i = start
            while i < len(nums):
                sub = self.nSumTarget(nums, n-1, i+1, target - nums[i])
                for arr in sub:
                    # (n-1)sum + nums[i] = target(nsum)
                    arr.append(nums[i])
                    res.append(arr)
                # skip over duplicates
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
        return res
