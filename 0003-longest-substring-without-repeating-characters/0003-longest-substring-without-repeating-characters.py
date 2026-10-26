class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        ans = 0  # <--- Initialize your answer variable to 0
        
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                # Instead of moving left by 1 once, we remove elements 
                # until the duplicate character is gone from our window
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                
            ans = max(ans, right - left + 1)
            
        return ans