## Array
## Binary Search
## Divide and Conquer

### Date: 07/20/2023

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)

        if l % 2: 
            return self.get_median(nums1, nums2, l // 2)
        else:
            return (self.get_median(nums1, nums2, l // 2) 
                    + self.get_median(nums1, nums2, l // 2 - 1)) / 2
        
    def get_median(self, nums1, nums2, k):

        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        i1, i2 = len(nums1) // 2 , len(nums2) // 2
        m1, m2 = nums1[i1], nums2[i2]

        # ensure that m1 is the smaller one
        if m1 > m2:
            m2, m1 = m1, m2
            i2, i1 = i1, i2
            nums1, nums2 = nums2, nums1

        # assume m1 is the largest possible median, 
        # it cannot exceed len(nums1) // 2 + len(nums2) // 2
        max_idx_m1 = len(nums1) // 2 + len(nums2) // 2

        # if max_idx_m1 < k, then the real median is not in nums1[:i1 + 1], 
        # we look within nums1[i1 + 1:] and nums2
        if max_idx_m1 < k:
            med = self.get_median(nums1[i1 + 1:], nums2, k - i1 - 1)
        else:
            med = self.get_median(nums1, nums2[:i2], k)
        
        return med
