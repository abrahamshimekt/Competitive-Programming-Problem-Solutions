class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = str(x)
        i,j = 0,len(num)-1

        # palindrome is a word the has the same meaning while reading from backward

        while i < j:
            if num[i] != num[j]:
                return False
            i +=1
            j -=1
            
        return True