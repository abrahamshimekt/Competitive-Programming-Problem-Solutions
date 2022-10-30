class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)
        k = 0
        output = []
        for num in nums1_count:
            if num in nums2_count:
                if nums2_count[num] <= nums1_count[num]:
                    k = nums2_count[num]
                    for j in range(k):
                        output.append(num)
                else:
                    k = nums1_count[num]
                    for j in range(k):
                        output.append(num)
        return output
    
    