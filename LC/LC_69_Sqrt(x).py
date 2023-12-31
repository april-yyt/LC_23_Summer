## Array

### Date: 07/22/2023

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                left = mid + 1
            else:
                right = mid - 1
        return right