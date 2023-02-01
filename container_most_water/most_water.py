class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            if height[left] <= height[right]:
                max_area = max(max_area,(right-left)*height[left])
                left +=1
            elif height[right] < height[left]:
                max_area = max(max_area,(right-left)*height[right])
                right -=1
        return max_area
        