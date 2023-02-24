class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left =0
        s1_substring = Counter(s1)
        substring = defaultdict(int)
        count = 0
        for right in range(len(s2)):
            substring[s2[right]] +=1
            count +=1
            if len(s1) == count:
                if s1_substring == substring:
                    return True
                
                substring[s2[left]] -=1
                if substring[s2[left]] == 0:
                    del substring[s2[left]]
                count-=1
                left +=1
        return False


            

        