## Sorting

### Date: 08/05/2023


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # use dict to count the occurrences of each element
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
        
        # number of keys is the number of unique elements
        unique_elements = len(d)

        curr_deleted = 0 # number of deleted elements
        count = 0 # number of considered elements
        for freq in sorted(d.values()):
            curr_deleted += freq
            count+=1
            if curr_deleted < k:
                continue
            elif curr_deleted == k: # we already deleted k elements
                return unique_elements - count # record the number of unique elements left
            else: # we already deleted more than k elements
                return unique_elements - (count-1)