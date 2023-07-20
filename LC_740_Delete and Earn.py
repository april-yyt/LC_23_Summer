## Array
## DP

### Date: 07/19/2023

#### Citadel

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 1. generate a dict which counts the occurence of each number
        cc = collections.Counter(nums)
        mx = max(cc)
        # 2. comp stores the total score
        comp = []

        for i in range(mx+1):
            for i in cc:
                comp.append(cc[i]*i)
            else:
                comp.append(0)
        # memo stores the calculated sub questions
        memo = [-1 for _ in range(mx+1)]

        # dynamic programming func for num i 
        def dp(i):
            if i < 0:
                return 0
            elif memo[i]>= 0:
                return memo[i]
            else:
                # for every element i, weve got 2 options: 1. delete i and i-2 for scoring, 2. delete i-1 for scoring
                # we choose the maximum score of the two
                res = max(dp(i-2)+comp[i],dp(i-1))
                memo[i] = res
                return res

        return dp(mx)

# TC: O(n)
# SC: O(n)