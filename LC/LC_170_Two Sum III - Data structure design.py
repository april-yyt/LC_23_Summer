## Array
## Binary Search

### Date: 07/24/2023

# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

class TwoSum:
    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self,value:int) -> bool:
        for key, val in self.nums.items():
            if key in self.nums and (value - key == key):
                if val > 1:
                    return True
            elif (value - key) in self.nums:
                return True
        return False