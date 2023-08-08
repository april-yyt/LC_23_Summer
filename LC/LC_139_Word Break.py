## Dynamic Programming

### Date: 08/08/2023

class Solution:
    def __init__(self):
        self.memo = []
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = [-1]*len(s)
        return self.dp(s,0,wordDict)

    def dp(self, s:str, i:int, wordDict:List[str])->bool:
        if i == len(s):
            return True
            # skip calculated word
        if self.memo[i] != -1:
            return True if self.memo[i]==1 else False
        # iterate over words and match s[i...]
        for word in wordDict:
            length = len(word)
            if i + length > len(s):
                continue
            sub_str = s[i:i+length]

            if sub_str != word:
                continue

            # if i is matched, check i+length
            if self.dp(s,i+length,wordDict):
                self.memo[i]=1
                return True

        self.memo[i]=0
        return False

