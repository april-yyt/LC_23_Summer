## Linked List

### Date: 07/29/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.r = random.Random()


        

    def getRandom(self) -> int:
        i, res = 0,0
        p = self.head
        while p:
            i += 1
            #generate an int between [0,i)
            #prob of this int ==0 is 1/i
            if 0 == self.r.randint(0,i-1):
                res = p.val
            p = p.next
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()