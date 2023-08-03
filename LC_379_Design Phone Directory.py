## Linked List

### Date: 08/02/2023

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.res = 0
        for i in range(maxNumbers):
            #  set the i-th bit of the number represented by self.res to 1.
            self.res |= 1<<i
        
    def get(self) -> int:
        first_set_bit = self.res & -self.res
        if first_set_bit == 0:
            return -1

        # get the bit pos of the first set bit
        pos = int(math.log(first_set_bit, 2))
        # mask this bit
        self.res ^= first_set_bit
        return pos
        
    def check(self, number: int) -> bool:
        num_,mask = 1<< number
        return True if self.res & num_mask == num_mask else False

    def release(self, number: int) -> None:
        rel = 1 << number
        self.res |= rel
        

###### O(1)
###### O(1)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)