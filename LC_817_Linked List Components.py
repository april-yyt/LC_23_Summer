## Linked List

### Date: 08/02/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        ans = 0
        s = set(nums)

        while(curr):
            if (curr.val in s and not(curr.next and curr.next.val in s)):
                ans += 1
            curr = curr.next
        return ans