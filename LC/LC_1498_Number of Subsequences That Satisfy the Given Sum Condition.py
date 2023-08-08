## Sorting

### Date: 08/05/2023

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums)-1
        c, mod = 0, (10**9+7)
        nums.sort()
        while i <= j:
            # if sum <= target, subsequence valid
            if nums[i]+nums[j] <= target:
                c += pow(2, (j-1), mod) # use pow for 2^(j-1) 
                i += 1
            else:
                j -= 1
        return c % mod
