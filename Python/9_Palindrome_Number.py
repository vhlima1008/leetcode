"""
LeetCode: 9 - Palindrome Number
Approach: Convert the integer to a string and compare mirrored characters from both ends to detect mismatch early.
Time: O(n) where n is the number of digits; Space: O(n) for the string/list representation.
"""

class Solution:
    def isPalindrome(self, x: int):
        state = False
        xArr = list(str(x))
        for i in range(len(xArr)):
            if (xArr[i] != xArr[-i-1]):
                return False
        return True

# test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(1000021))
