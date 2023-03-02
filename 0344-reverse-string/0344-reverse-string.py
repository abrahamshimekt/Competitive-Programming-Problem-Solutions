class Solution:
    def reverse_s(self,l,r,s):
        if l >= r:
            return 
        s[r],s[l] = s[l],s[r]
        return self.reverse_s(l+1,r-1,s)
             
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverse_s(0,len(s)-1,s)
        