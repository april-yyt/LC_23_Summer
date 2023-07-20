## Array
## Backtracking

### Date: 07/20/2023

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def bt(start, total, path):
            if total == target:
                ans.append(path)
                return 
            
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    return 
                # skip duplicates
                elif i > start and candidates[i] == candidates[i-1]:
                    continue
                else:
                    bt(i + 1, total + candidates[i], path + [candidates[i]])

        bt(0, 0, [])
        return ans