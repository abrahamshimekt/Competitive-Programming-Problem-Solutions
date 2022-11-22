class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        i = 0
        kBeauty = 0
        while i + k <= len(s):
            if int(s[i:k+i]) != 0 and num % int(s[i:k+i]) == 0:
                kBeauty +=1
            i +=1
        return kBeauty
            