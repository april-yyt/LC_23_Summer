## String
## Hash
### Date: 08/14/2023

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = dict()
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic:
            if dic[i]==1:
                return s.index(i)
        return -1
