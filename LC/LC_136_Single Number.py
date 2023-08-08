## Hash

### Date: 08/08/2023

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0)+1
        return min(my_dict, key=my_dict.get) # get the key with min value