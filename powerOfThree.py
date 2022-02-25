class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n>1:
            if n%3 !=0:
                return False
            n /=3
        return n ==1
        # if n ==0:
        #     return False
        # x = str(math.log(n,3))
        # for i in range(len(x)):
        #     if x[i] == '.' and x [i + 1] =='0':
        #         return True
        # return False