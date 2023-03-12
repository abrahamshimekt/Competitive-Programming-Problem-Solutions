class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = [0,float("inf")]
        comparator = defaultdict(int)
        t = Counter(t)
        k = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in t:
                continue
            else:
                comparator[s[right]] +=1
                if comparator[s[right]] == t[s[right]]:
                    k +=1
                while  k== len(t):
                    
                    if right-left+1 < window[1]-window[0]:
                        window = [left,right+1]
                    if s[left] not in t:
                        
                        left +=1
                    elif comparator[s[left]] > t[s[left]]:
                        comparator[s[left]] -=1
                        left +=1
                    else:
                        break
        if window[1] == float('inf'):
            return ''
        return s[window[0]:window[1]]
        
            
            