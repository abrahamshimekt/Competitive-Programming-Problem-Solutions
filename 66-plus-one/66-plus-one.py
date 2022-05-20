class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_digit = ""
        for i in range(len(digits)):
            s_digit +=str(digits[i])
        ans =[]
        s_digit = str(int(s_digit) + 1)
        for digit in s_digit:
            ans.append(int(digit))
        return ans
    
        