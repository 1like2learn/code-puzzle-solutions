"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8

https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = [{"openings": 1, "string": "("}]
        output = []
        
        for item in queue:
            if len(item["string"]) < n * 2:
                # if there are more open parenthesis than the final length
                # minus the length of the current string
                if ((n * 2) - len(item["string"])) > item["openings"]:
                     queue.append(
                         {
                             "string": item["string"] + '(',
                             "openings": item["openings"] + 1
                         }
                     )
                if item["openings"] > 0:
                     queue.append(
                         {
                             "string": item["string"] + ')',
                             "openings": item["openings"] - 1
                         }
                     )
            else:
                output.append(item["string"])
        print(queue)
        return output