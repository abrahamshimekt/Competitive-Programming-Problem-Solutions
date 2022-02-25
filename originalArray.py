from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        original = []
        if counter[0] % 2 !=0: 
            return []
        else:
            original.extend([0] * (counter[0]//2))
            
        for i in sorted(counter):
            if counter[i] > counter[2 * i]:
                return []
            if i:
                counter[2 * i] -= counter[i]
                original.extend([i] * counter[i])
            
        return original
#         changed.sort()
#         n = len(changed)
#         original = []
#         if changed == [0]* n:
#             if n % 2 ==0:
#                 original = changed[:n//2]
#             else:
#                 original = []
#         for i in range(n-1):
#             for j in range(i + 1,n):
#                 if changed[j] == 2* changed[i] and changed[i] != changed[j]:
#                     original.append(changed[i])
                 
#         return original
        