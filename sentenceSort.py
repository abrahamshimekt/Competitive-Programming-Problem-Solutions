class Solution:
    def sortSentence(self, s: str) -> str:
        sL = s.split()
        n = len(sL)
        for i in range(n):
            for j in range(n-1):
                if sL[j][-1] > sL[j + 1][-1]:
                    sL[j],sL[j + 1] = sL[j + 1],sL[j]
        for k in range(n):
            sL[k] = sL[k][:-1]
        return " ".join(sL)