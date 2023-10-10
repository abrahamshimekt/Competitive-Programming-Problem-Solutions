class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
        m = len(s1)
        n = len(s2)
        s1Hash = defaultdict(int)
        for i in range(m):
            s1Hash[s1[i]] += 1
        left = 0
        s2Hash = defaultdict(int)
        for right in range(n):
            s2Hash[s2[right]] += 1
            if right -left + 1 == m:
                if s1Hash == s2Hash:
                    return True
                else:
                    s2Hash[s2[left]] -=1

                    if s2Hash[s2[left]] == 0:
                        del s2Hash[s2[left]]
                    left +=1
        return False

