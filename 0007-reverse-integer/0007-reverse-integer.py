class Solution:
    def reverse(self, x: int) -> int:
        reversedInt = ''
        isNegative = False
            
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
            
        for i in str(x):
            if i == "-":
                isNegative = True
            else:     
                reversedInt = i + reversedInt
        reversedInt = int(reversedInt)
        
        if isNegative: reversedInt *= -1
        if reversedInt < INT_MIN or reversedInt > INT_MAX: reversedInt = 0
        return reversedInt
        