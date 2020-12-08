"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Constraints
    n = height.length
    2 <= n <= 3 * 104
    0 <= height[i] <= 3 * 104

https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        largestVolume = 0
        
        i = 0
        j = len(height) - 1
        
        while j != i:
            curVolume = (height[i] if height[i] < height[j] else height[j]) * (j - i)
            if curVolume > largestVolume:
                largestVolume = curVolume
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
                
        return largestVolume