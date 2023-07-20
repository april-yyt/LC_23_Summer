## Array

### Date: 07/17/2023

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      res = []
      # sort accrd to the start of the intervals
      intervals.sort(key = lambda a:a[0])

      res.append(intervals[0])
      for curr in intervals[1:]:
        last = res[-1]
        # curr[0]: start of the next interval for merge
        # last[1]: end of the last interval in results
        # if next start is smaller/eq to the last end, perform merge
        # set the last end to the next end 
        if curr[0] <= last[1]:
            last[1]=max(last[1], curr[1])
        else:
            # move ptr to the next interval for merging
            res.append(curr)
        return res