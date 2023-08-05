## Array
## Hash Table
## Prefix Sum

### Date: 07/19/2023

#### Citadel

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # for any subarray nums[i:j] if the sum is divisible by K, then sum(nums[:i]) % K == sum(nums[:j]) % K
        # since j-i is divisible by K, so sum(nums[i:j]) % K == 0
        li = [0]*k
        n = len(nums)
        sm = 0
        for i in range(n):
            sm += nums[i]
            # count the number of prefix sum that has the same remainder
            li[sm%k] += 1
        st = li[0]
        count = (st*(2+(st-1))) // 2

        for i in range(1,k):
            x = li[i]
            count += (x*(x-1)) // 2
        return count