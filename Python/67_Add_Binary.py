class Solution:
    def binaryToDecimal(self, bin):
        convert = 0
        binaryLen = len(bin)
        for i in range(binaryLen):
            bit = int(bin[i])
            convert += bit * (2 ** (binaryLen - i - 1))
        return convert
    
    def decimalToBinary(self, dec):
        convert = ''
        while True:
            if (dec % 2 != 0):
                convert = '1' + convert
            else:
                convert = '0' + convert
            dec = int(dec // 2)
            if (dec == 0):
                break
        return convert
    
    def addBinary(self, a: str, b: str):
        binA = self.binaryToDecimal(a)
        binB = self.binaryToDecimal(b)
        sumAB = binA + binB
        sumAB = self.decimalToBinary(sumAB)
        return sumAB

# test
sol = Solution()
print(sol.addBinary('100', '101'))

# best solution
# 
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         ret = int(a, 2) + int(b, 2)
#         return bin(ret)[2:]