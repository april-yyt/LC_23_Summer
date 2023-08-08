## Hash

### Date: 08/07/2023

import collections


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        res = []
        for i in range(1,len(words)):
            tmp = tmp & collections.Counter(words[i]) # & would grant 0 if any is 0
        
        # output everything left in res list
        for j in tmp:
            v = tmp[j]
            while(v):
                res.append(j)
                v -= 1
        return res
