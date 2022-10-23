class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_index = {}
        stack = []
        for i in range(len(nums2)):
            nums2_index[nums2[i]] = i
        for x in nums1:
            get= False
            for y in nums2[nums2_index[x]+1:]:
                if y> x:
                    get = True
                    stack.append(y)
                    break
            if not get:
                stack.append(-1)
        return stack
                    
        