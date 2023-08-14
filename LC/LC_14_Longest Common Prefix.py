## String
### Date: 08/14/2023

# view the string as a 2d array
# 1st dim is the number of words in the strs array
# 2nd dim is the number of columns, take the first word as benchmark

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs)
        n = len(strs[0])
        for col in range(n):
            for row in range(1,m):
                this, prev = strs[row], strs[row-1]
                if col >= len(this) or col >= len(prev) or this[col] != prev[col]:
                    return strs[row][:col]
        return strs[0]
