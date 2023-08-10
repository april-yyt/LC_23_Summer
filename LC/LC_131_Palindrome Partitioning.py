## Array
## String

### Date: 08/09/2023

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    
    def partition(self, s: str) -> List[List[str]]:
        self.backtrack(s,0)
        return self.res
        
    def backtrack(self, s:str, start:int):
        if start == len(s):
            self.res.append(self.track[:])
        for i in range(start,len(s)):
            if not self.isPalindrome(s,start,i):
                continue
            self.track.append(s[start:i+1])
            self.backtrack(s,i+1)
            self.track.pop()

    def isPalindrome(self,s:str, start:int, end:int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True 