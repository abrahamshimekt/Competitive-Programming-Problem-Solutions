class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashMap = Counter(arr)
        for num in arr:
            if num == 0 and hashMap[num] <2:
                continue
            elif num*2 in hashMap:
                return True
        return False