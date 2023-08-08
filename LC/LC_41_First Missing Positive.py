## Hash

### Date: 08/08/2023

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # store occurences in d
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
        # find first missing positive
        for i in range(1,len(nums)+1):
            if i not in d:
                return i
        else:
            return len(nums)+1