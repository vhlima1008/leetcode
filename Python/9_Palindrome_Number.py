class Solution:
    def isPalindrome(self, x: int):
        state = False
        xArr = list(str(x))
        for i in range(len(xArr)):
            if (xArr[i] != xArr[-i-1]):
                return False
        return True

# test
sol = Solution()
print(sol.isPalindrome(1000021))