class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # memo : (key, value)
        # memo : (function_param, returned value for that call )
        if n== 0:
            return 0
        nums = {0:0,1:1}
        
        def getMax(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return nums[1]
            if n == 2:
                return 1
        
            if nums.get(n,None):
                return nums[n]
            i = n//2
            one = getMax(i+1)
            second = getMax(i)

            if n % 2:

                nums[n] = one + second #odd
                
            else:
                nums[n] = second #even

            return nums[n]
        for index in range(n,n//2,-1):
            getMax(index)

        return max(nums.values())
            

                
        
