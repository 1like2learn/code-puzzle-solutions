class Solution:
    def isValid(self, s: str) -> bool:
        openingChar = {'(','{','['}
        closingChar = {
            '}': '{',
            ']': '[', 
            ')': '('
        }
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