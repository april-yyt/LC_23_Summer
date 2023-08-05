## Array
## Binary Search

### Date: 07/24/2023

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        i, j, last_space = 0, len(s)-1, -1

        def do_word(st, en):
            nonlocal s
            start, end = start+1, end-1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start +=1
                end -=1

        while i < j:
            s[i], s[j] = s[j], s[i]
            # whenver we encounter a space, do_word to reverse the word before the space
            if s[i] == ' ':
                do_word(last_space, i)
                last_space = i
            i += 1
            j -= 1
        while i < len(s):
            if s[i] == ' ':
                do_word(last_space, i)
                last_space = i
            i += 1
        do_word(last_space, i)
