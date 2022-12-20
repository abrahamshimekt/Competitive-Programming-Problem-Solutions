def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter  = 0
        i = 0
        while i + 3 <= len(nums):
            curr_triangle = nums[i:i + 3]
            if curr_triangle[0] + curr_triangle[1] > curr_triangle[2]:
                max_perimeter = max(max_perimeter,sum(curr_triangle))
            i +=1
        return max_perimeter