class Solution:
    def isValid(self, s: str) -> bool:
        openingChar = {'(','{','['}
        closingChar = {
            '}': '{',
            ']': '[', 
            ')': '('
        }
        # The stack represents the open parenthesis. The most recent parenthesis
        # needs to be the first to be closed.
        stack = []
        for char in s:
            if char in openingChar:
                stack.append(char)
            elif char in closingChar:
                if len(stack) > 0 and closingChar[char] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        if len(stack) == 0:
            return True
        else:
            return False