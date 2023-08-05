## Linked List
## Stack

### Date: 07/28/2023


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0,0
        # calculate num1 and num2
        while l1!=None:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        while l2!= None:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        dummyList = dummy = ListNode(0)

        ans = str(num1 + num2)
        for i in ans:
            dummy.next = ListNode(i)
            dummy = dummy.next
        
        return dummyList.next


