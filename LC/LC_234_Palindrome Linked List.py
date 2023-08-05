## Array
## 2 Pointers

### Date: 07/24/2023

#Definition for singly-linked list.
#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # find the midpoint
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # check if the two halves are equal
        p1 = head
        p2 = head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True