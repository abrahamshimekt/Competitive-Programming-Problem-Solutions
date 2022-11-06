class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_hashmap = Counter(nums1)
        nums2_hashmap = Counter(nums2)
        index_0 = []
        index_1 = []
        for num in nums1_hashmap :
            if num not in nums2_hashmap:
                index_0.append(num)
        for num in nums2_hashmap :
            if num not in nums1_hashmap:
                index_1.append(num)
        return [index_0,index_1]
        