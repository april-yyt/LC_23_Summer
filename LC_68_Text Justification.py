## Array
## String

### Date: 07/23/2023

class Solution:
    def fullJustify(self, words, maxWidth):
        # res for results
        # cur for current line
        # num_of_letters for the number of letters in current line
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += " "
                res.append(" ".join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [" ".join(cur).ljust(maxWidth)]