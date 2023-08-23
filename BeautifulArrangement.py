class Solution(object):
    def backTrack(self,nums, perm):
        if len(nums) == 0 and len(perm) == self.n:
            self.beautifuls += 1
        else:
            for index in range(len(nums)):
                if (not nums[index] % (len(perm)+1)) or (not ((len(perm)+1) % nums[index])):
                    perm.append(nums[index])
                    remain = nums[:index] + nums[index+1:]
                    self.backTrack(remain, perm)
                    perm.pop()
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        nums = [num for num in range(1, n+1)]
        self.beautifuls = 0 
        self.backTrack(nums, [])

        return self.beautifuls
