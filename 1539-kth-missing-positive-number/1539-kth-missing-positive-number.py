class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        hashmap = Counter(arr)
        for i in range(1,2001):
            if i not in hashmap and k >0:
                k -=1
            if k == 0:
                return i
        
                
        
        
        