## Sorting
## 2 Pointers

### Date: 08/05/2023

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # lo and hi points to the lightest and heavyiest person
        lo, hi = 0, len(people)-1
        boats = 0

        while lo <= hi: # pair the lightest and heavyiest person in a boat
            if people[lo]+people[hi] <= limit:
                # current lo and hi can share a boat, move on to the next
                lo += 1
                hi -= 1
            else:
                # else the current heaviest should take one boat alone
                hi -= 1
            boats += 1

        return boats

