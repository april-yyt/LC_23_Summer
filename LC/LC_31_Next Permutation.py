## Array

### Date: 07/18/2023

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # base case
        # if nums is sorted in decreasing order, then theres no next greater permutation
        # we just return the smallest permutation(the array sorted in increasing order)
        if nums == sorted(nums, key=lambda x:-x):
            nums.sort()
            return
        # all the loops are reverse since we start from the right
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                # find the first position that has nums[i-1] < nums[i]
                min_idx, min_val = len(nums), float('inf')
                # find the smallest permutation greater than nums[i-1], from permutations starting from nums[i]
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1] and nums[j] < min_val:
                        min_val = nums[j]
                        min_idx = j
                # do the swap
                nums[i-1], nums[min_idx] = nums[min_idx], nums[i-1]

                # sort the rest of the array, bubble sort
                while True:
                    swapped = False
                    for k in range(i, len(nums)-1):
                        if nums[k] > nums[k+1]:
                            swapped = True
                            nums[k], nums[k+1] = nums[k+1], nums[k]
                    if swapped == False:
                        break
                return