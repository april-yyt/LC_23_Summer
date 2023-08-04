## Array
## Sorting
## String

### Date: 08/03/2023

class Solution:
    def largestNumber(self, nums:List[int]) -> str:
        res = ""
        for i in nums:
            i = str(i)
        for i in range(len(nums)):
            # iterate over all combinations of i and i+1 to the end of the array
            for j in range(i+1, len(nums)):
                if str(nums[i])+str(nums[j]) > str(nums[j])+str(nums[i]):
                    # compare xy and yx, if xy is larger than yx remain the same
                    continue
                else:
                    # compare xy and yx, if xy is smaller than yx swap them
                    nums[i], nums[j] = nums[j], nums[i]
        res = "".join(str(i) for i in nums) # joining the list
        if int(res) == 0:
            return "0"
        return res