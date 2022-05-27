class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num ==1:
            return False
        sum_ = 1
        i = 2
        while i <= pow(num,0.5):
            if num % i ==0:
                sum_ += (i + num/i)
            i +=1
        
        return sum_ ==num
            