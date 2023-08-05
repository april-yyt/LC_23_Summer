## Array
## Binary Search

### Date: 07/20/2023


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(left,right,pivot)->int:
            while left <= right:
                print(left,right)
                mid = left + (right - left)//2
                # mid+pivot -> the midpoint of the rotated array
                # since it may exceed the length of the array, we take the mod
                if nums[(mid+pivot) % len(nums)] > target:
                    right = mid - 1
                elif nums[(mid+pivot) % len(nums)] < target:
                    left = mid + 1
                else:
                    return (mid+pivot) % len(nums)
            return -1
        
        # step 1 is to find the index of the pivot
        pivot = nums.index(min(nums))
        left,right = 0, len(nums)-1
        # step 2 is to binary search on the array for the target
        index = binarySearch(left, right, pivot)

        return index


