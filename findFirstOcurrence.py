class Solution:
    def strStr(self, s: str, pattern: str) -> int:
        n = len(s)
        m = len(pattern)

        if m == 0:
            return 0

        lps = [0] * m

        i = 1
        length = 0

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        i = 0
        j = 0
        while i < n:
            if s[i] == pattern[j]:
                i += 1
                j += 1
                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
