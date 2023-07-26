## Linked List
## 2 Pointers

### Date: 07/25/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr stores all the extracted values
        arr, itr = [], head
        # itr thru the list and copy
        while itr:
            arr.append(itr.val)
            itr = itr.next
        arr.sort()
        itr = head
        i = 0

        # fill the sorted values
        while itr:
            itr.val = arr[i]
            i += 1
            itr = itr.next
        return head