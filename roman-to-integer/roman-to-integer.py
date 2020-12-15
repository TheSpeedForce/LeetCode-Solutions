class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        temp = s[::-1]
        result = roman[temp[0]]
        if len(temp) == 1:
            return result
        for i in range(len(temp)-1):
            if roman[temp[i+1]] < roman[temp[i]]:
                result -= roman[temp[i+1]]
            else:
                result += roman[temp[i+1]]
                
        return result
