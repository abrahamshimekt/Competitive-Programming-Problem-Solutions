class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        m = len(b)
        lps = [0]*m
        length = 0
        index = 1
        while index < m:
            if b[index] == b[length]:
                length +=1
                lps[index] = length
                index +=1
            elif length == 0:
                lps[index] = 0
                index +=1
            else:
                length = lps[length-1]
        n = len(a)
        i = 0
        j = 0
        steps = 1
        while i < n and steps <= ceil(m/n) + 1:
            if a[i] == b[j]:
                i +=1
                j +=1
                if j == m:
                    return steps
                if i == n:
                    steps +=1
                i %= n
            elif j!= 0:
                j = lps[j-1]
            else:
                i +=1
                if i==n:
                    steps +=1
                i %=n
        return -1

        
