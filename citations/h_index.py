class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left =-1
        right = len(citations)
        while right -left > 1:
            mid = left + (right -left)//2
            if len(citations)-mid <= citations[mid]:
                right = mid
            else:
                left = mid
        return len(citations)-right