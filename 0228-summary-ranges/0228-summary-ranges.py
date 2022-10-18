class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=j=0
        output = []
        while j < len(nums):
            if j <  len(nums) -1 and nums[j+1]-nums[j] == 1 :
                j +=1
            else:
                if i==j:
                    output.append(f"{nums[i]}")
                    i +=1
                    j +=1
                else:
                    output.append(f"{nums[i]}->{nums[j]}")
                    j +=1
                    i = j
        return output
        