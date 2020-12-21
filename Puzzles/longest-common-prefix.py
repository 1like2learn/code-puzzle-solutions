"""
    i represents the index of the current character we are checking
    We loop until one of the exit conditions are met.
    
    Every iteration of the parent loop increases i, moving on to the next character. 
    It also loops through all the provided strings, checking to make sure they have
    the same character at any given index. If there is a different character or the
    string does not have the given index the loop will end and return the correct value.
    
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        
        while True:
            try:
                curChar = strs[0][i]
            # Incase the first string is the shortest and i is no longer a valid index.
            except IndexError:
                try:
                    return strs[0]
                # Incase strs is empty
                except IndexError:
                    return "";
            for string in strs:
                try:
                    # Incase the characters don't match
                    if curChar != string[i]:
                        return string[:i]
                # Incase i is not a valid index on the string.
                except IndexError:
                    return string[:i]
            i += 1