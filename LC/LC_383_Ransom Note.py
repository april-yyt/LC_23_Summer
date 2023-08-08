## Hash

### Date: 08/07/2023

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # letters in magazine cannot be reused
        # all letters are lower case
        ransom_count = [0]*26
        magazine_count = [0]*26
        for c in ransomNote:
            # ord(c)-ord('a) is usually used as the hash function for lower case letters
            ransom_count[ord(c)-ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c)-ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))