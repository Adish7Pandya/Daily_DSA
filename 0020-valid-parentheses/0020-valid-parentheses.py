class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'()','{}','[]'}
        for char in s:

            if char in '{[(':
                stack.append(char)
            else: 
                if not stack or stack[-1]+char not in valid:
                    return False
                stack.pop()

        return not stack 
        