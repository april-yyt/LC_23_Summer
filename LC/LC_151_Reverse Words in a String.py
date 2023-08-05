## String
## 2 Pointers

### Date: 07/25/2023

class Solution:
    def reverseWords(self, s: str) -> str:
        tmp = s.split()
        tmp.reverse()
        return " ".join(tmp)

        