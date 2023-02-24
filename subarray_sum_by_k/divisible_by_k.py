class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        i=count=remainder=0
        prefix_remainder = {0:1}
        while i < len(nums): 
            remainder = (remainder +nums[i]) %k
            if remainder < 0:
                remainder += k
            if remainder in prefix_remainder:
                count += prefix_remainder[remainder]
                prefix_remainder[remainder] +=1
            else:
                prefix_remainder[remainder] =1
            i +=1
        return count