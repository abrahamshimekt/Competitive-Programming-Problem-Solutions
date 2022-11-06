class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hashmap = Counter(nums1)
        nums2_hashmap = Counter(nums2)
        output = []
        for num in nums1_hashmap:
            if num in nums2_hashmap:
                output.append(num)
        return output
            