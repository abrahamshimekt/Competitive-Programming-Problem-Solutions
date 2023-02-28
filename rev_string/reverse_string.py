class Solution:
    def reverse_list(self,l,r,s):
        if l>=r:
            return s
        s[l],s[r] = s[r],s[l]
        return self.reverse_list(l+1,r-1,s)
                                     
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverse_list(0,len(s)-1,s)