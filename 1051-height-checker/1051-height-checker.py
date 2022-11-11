class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = len(expected)
        numIdices = 0
        for i in range(n):
            if expected[i] != heights[i]:
                numIdices +=1
        return numIdices
            