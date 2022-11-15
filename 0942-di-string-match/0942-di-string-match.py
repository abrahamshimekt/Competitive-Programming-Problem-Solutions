class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        perm = []
        for i in range(n+1):
            perm.append(i)
        for j in range(n):
            if s[j] == "D":
                temp = perm.pop()
                perm.insert(j,temp)
        return perm
        
        