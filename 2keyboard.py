class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 0
        factors = []
        for factor in range(1,n//2+1):
            if n% factor == 0:
                factors.append(factor)
        minOperation = float("inf")
        for f in factors:
            if f == 1:
                minOperation = min(minOperation,n)
            else:
                minOperation = min(minOperation, f+1 + (n-f)//f)
        return minOperation

