"""
LeetCode: 13 - Roman to Integer
Approach: Given a roman numeral, convert it to an integer.
Time: O(n)
"""

class Solution:
    def romanToInt(self, s: str):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        integer = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]: 
                integer -= roman[s[i]]
            else: 
                integer += roman[s[i]]
                
        return integer + roman[s[-1]]
                
# test
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))