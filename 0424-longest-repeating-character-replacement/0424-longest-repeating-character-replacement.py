class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {}
        right = 0
        count = 0
        n = len(s)
        while right < n:
            seen[s[right]]= seen.get(s[right],0)+1

            while (right-left +1) - max(seen.values())>k:
                seen[s[left]]-=1
                left+=1
            count = max(count,right - left+1)
            right+=1
        return count