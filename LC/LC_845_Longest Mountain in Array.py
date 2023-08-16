## 2 Ptrs
### Date: 08/15/2023


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count =0
        ans=0
        n=len(arr)
        for i in range(1,n-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                count = 1
                p = i
                q = i
                while (p>0 and arr[p]>arr[p-1]):
                    count += 1
                    p -= 1
                while (q<n-1 and arr[q]>arr[q+1]):
                    q+= 1
                    count += 1
            ans = max(count,ans)
            count =0
        return ans