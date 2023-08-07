## Sorting

### Date: 08/05/2023

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        i,j = 0, len(nums)-1
        while i <= j:
            if nums[i]+nums[j] > target:
                # examine the next largest element
                j -= 1
            else:
                # any element from i to j-1 can be included in the sequence
                ans += 2 **(j-1)
                ans  = ans % (10**9+7)
                i += 1
        return ans%(10*9+7)
