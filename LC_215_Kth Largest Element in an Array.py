## Array
## Sorting

### Date: 08/03/2023

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        pq = []
        for e in nums:
            heapq.heappush(pq, e)
            # when num of elements in the heap is greater than k, remove the element at the heap top
            if len(pq) > k:
                heapq.heappop(pq)
        # left in the heap are the k largest elements
        # top of the heap is the smallest among them
        # i.e. the kth largest element
        return pq[0]
