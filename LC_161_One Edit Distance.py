## Array
## Binary Search

### Date: 07/24/2023

""" 
A string s is said to be one distance apart from a string t if you can:
- Insert exactly one character into s to get t.
- Delete exactly one character from s to get t.
- Replace exactly one character of s with a different character to get t.
 """

from collections import deque
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        q_s = deque(s)
        for c in s:
            q_s.append(c)
        
        left, right = 0, len(t)-1
        while left <= right:
            if q_s and t[left] == q_s[0]:
                # if same, we pop the first element in q_s
                # and move the left ptr, indicating that this char is processed
                q_s.popleft()
                left = left + 1
            elif q_s and t[right] == q_s[-1]:
                q_s.pop()
                riight -= 1
            else:
                break
        return (len(q_s) == 1 and left > right) or(not q_s and l == r) or (len(q_s) == 1 and left == right)
