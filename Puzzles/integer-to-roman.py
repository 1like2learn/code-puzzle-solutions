"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Constraints

    1 <= num <= 3999

https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        
        while num >= 1000:
            num -= 1000
            output += 'M'
            
        if num >= 900:
            num -= 900
            output += "CM"
            
        while num >= 500:
            num -= 500
            output += 'D'
            
        if num >= 400:
            num -= 400
            output += "CD"
            
        while num >= 100:
            num -= 100
            output += 'C'
                
        if num >= 90:
            num -= 90
            output += "XC"
            
        while num >= 50:
            num -= 50
            output += 'L'
        
        if num >= 40:
            num -= 40
            output += "XL"
            
        while num >= 10:
            num -= 10
            output += 'X'
            
        if num >= 9:
            num -= 9
            output += "IX"
            
        while num >= 5:
            num -= 5
            output += 'V'
            
        if num >= 4:
            num -= 4
            output += "IV"
            
        while num >= 1:
            num -= 1
            output += 'I'
            
        return output