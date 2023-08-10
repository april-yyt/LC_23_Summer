## Hash

### Date: 08/09/2023

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        y = 0 # y is x-reveresed
        while tmp > 0:
            last_num = tmp % 10
            tmp = tmp // 10
            y = y * 10 + last_num
        return y == x
