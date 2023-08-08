## Array
## 2 Pointers


### Date: 08/07/2023


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        # delta tracks the difference between current sum and target
        delta = float('inf')
        for i in range(len(nums)-2):
            # fix nums[i] as one of the three
            # call twoSumClosest to find the two remaining elements that combines to the closest sum
            sum_ = nums[i]+ self.twoSumClosest(nums, i+1, target-nums[i])
            # if a closer sum is found, update delta
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
        return target - delta

    def twoSumClosest(self, nums: List[int], start:int, target:int):
        lo, hi = start, len(nums)-1
        delta = float('inf')
        while lo < hi:
            sum_ = nums[lo]+nums[hi]
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
            if sum_ < target:
                lo += 1
            else:
                hi -= 1
        return target - delta

