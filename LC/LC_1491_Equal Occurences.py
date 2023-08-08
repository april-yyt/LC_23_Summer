## Hash

### Date: 08/08/2023


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        rec = {}
        for c in s:
            rec[c] = rec.get(c,0)+1
        key_values = rec.values() 
        # if all occurences are the same, 
        # there should only be one value in the rec dict
        return len(set(key_values)) == 1 # use set to eliminate dup