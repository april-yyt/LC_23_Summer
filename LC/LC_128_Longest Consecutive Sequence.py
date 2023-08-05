## Array

### Date: 07/23/2023


""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time. """

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set removes duplicates
        nums = sorted(set(nums))

        curr_max = 0 # current known longest consecutive length
        curr_count = 0 # current consecutive length
        prev = None
        for i in nums:
            if prev is not None:
                if prev + 1 == i: # if the previous is consecutive to the current
                    curr_count += 1
                else: # otherwise a sequence is broken
                    curr_max = max(curr_max, curr_count)
                    curr_count = 1
            else:
                curr_count += 1
            prev = i
        return max(curr_max, curr_count)
