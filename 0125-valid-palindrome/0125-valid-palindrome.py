class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # 1. Skip non-alphanumeric characters from the left
            if not s[left].isalnum():
                left += 1
            # 2. Skip non-alphanumeric characters from the right
            elif not s[right].isalnum():
                right -= 1
            # 3. Compare valid characters
            else:
                if s[left].lower() != s[right].lower():
                    # If any pair doesn't match, it's NOT a palindrome
                    return False
                # If they match, move both pointers inward
                left += 1
                right -= 1
                
        # If we get through the whole loop, it IS a palindrome
        return True