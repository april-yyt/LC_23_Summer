## Sorting

### Date: 08/04/2023

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
        #  the majority element occurs more than n/2 times
        # when the array is sorted, it will occupy the middle position