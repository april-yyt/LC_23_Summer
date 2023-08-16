## 2 Ptrs
### Date: 08/15/2023

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        slow = fast = float('inf')
        for n in nums:
            if n <= slow:
                slow = n
            elif n <= fast:
                fast = n
            else:
                return True
        return False