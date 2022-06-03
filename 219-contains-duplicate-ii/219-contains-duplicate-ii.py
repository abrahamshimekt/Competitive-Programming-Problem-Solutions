class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable and i - hashTable.get(nums[i],None) <= k:
                return True
            else:
                hashTable[nums[i]] = i
        return False