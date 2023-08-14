## String
### Date: 08/14/2023

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000) # must add this line.....
        return str(int(num1)+int(num2))
