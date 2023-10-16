class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}
        def miximizeUncrosedLines(i,j):
            if i< 0 or j < 0:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if nums1[i] == nums2[j]:
                result = 1 + miximizeUncrosedLines(i-1,j-1)
            
            else:
                result = max(miximizeUncrosedLines(i-1,j),miximizeUncrosedLines(i,j-1))
            dp[(i,j)] = result
            return dp[(i,j)]
        n = len(nums1)-1
        m = len(nums2)-1
        return miximizeUncrosedLines(n,m)
        
