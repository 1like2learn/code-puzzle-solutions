"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case),

"""
class Solution:
    """
    Start by checking for a few edge cases. Either the string is 1 long, the string is two identical characters or the string is two different characters. These must be done seperately due to out of bound index concerns

    Create a queue with the two possible starting points and a array that stores the index of the longest substring that defaults to have a value of nothing.

    For every coordinate in the queue check if it is a palindrome and expand until it is the largest possible palindrome from this start point. If these compare these coordinates to the greatest and keep the one with the greatest difference.

    Once all starting points have been checked return the substring with the coordinates stored in longest.
    """
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        if length == 1 or (s[0] != s[1] and length == 2):
            return s[0]
        elif length == 2:
            return s
        longest = [0, 0]
        queue = [[0,1],[0,2]]
        
        for coords in queue:
            start = coords[0]
            end = coords[1]
            if end < length - 1:
                queue.append([start + 1, end + 1])
            if s[start] == s[end]:
                while start > 0 and end < length - 1 and s[start - 1] == s[end + 1]:
                    start -= 1
                    end += 1
            if end - start > longest[1] - longest[0] and s[start] == s[end]:
                longest = [start, end]
        return s[longest[0]:longest[1] + 1]
    
    """
    Make a queue with every possible substring until you find a substring that is a palindrome.
    """
    def checkIfPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            
    def longestPalindromeFailed(self, s: str) -> str:
        longest = f"{s[0]}"
        cache = set()
        queue = [s]
        for curString in queue:
            if curString[0] == curString[-1]:
                if self.checkIfPalindrome(curString):
                    return curString
            if len(curString) > 1:
                if curString[1:] not in cache:
                    queue.append(curString[1:])
                    cache.add(curString[1:])
                if curString[:-1] not in cache:
                    queue.append(curString[:-1])
                    cache.add(curString[:-1])
        return longest