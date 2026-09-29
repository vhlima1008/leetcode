class Solution:
    def myAtoi(self, s: str) -> int:
        convertedString = 0
        stringReceived = s.strip()
        isNegative = False
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if not stringReceived: return 0
        
        if stringReceived.startswith("-"): 
            isNegative = True
            stringReceived = stringReceived.removeprefix("-")
        elif stringReceived.startswith("+"):
            stringReceived = stringReceived.removeprefix("+")
            
        for i in stringReceived:
            if i.isdigit():
                convertedString = convertedString * 10 + int(i)
            else: break
                
        if isNegative: convertedString *= -1
        if convertedString < INT_MIN: convertedString = INT_MIN
        if convertedString > INT_MAX: convertedString = INT_MAX
        
        return convertedString
