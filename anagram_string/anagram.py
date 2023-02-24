class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []
        curr = defaultdict(int)
        for right in range(len(s)):
            curr[s[right]] +=1
            if right-left +1 == len(p):
                if curr == Counter(p):
                    result.append(left)
                curr[s[left]] -= 1
                if curr[s[left]] == 0:
                    del curr[s[left]]
                left +=1
        return result



        


                
            
        