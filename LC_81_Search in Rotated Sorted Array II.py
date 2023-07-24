## Array
## Binary Search

### Date: 07/23/2023

""" Given the array nums after the rotation and an integer target, 
return true if target is in nums, or false if it is not in nums. """

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = low+(high-low)//2
            print(mid, end=" ")
            # use binary search to find the mid of the array, 
            # then check if the target is in the left or right half
            if target == nums[mid]:
                return True
            if (nums[mid]==nums[low]) and (nums[mid]==nums[high]):
                low += 1
                high -= 1
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
