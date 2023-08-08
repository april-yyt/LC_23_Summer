## Hash

### Date: 08/08/2023

from collections import Counter
class Solution:
    def intersect(self,nums1:List[int],nums2:List[int]) -> List[int]:
        result = []
        x = Counter(nums1) & Counter(nums2)
        for i, j in x.items():
            result.append([i]*j)
        return result