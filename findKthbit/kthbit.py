class Solution:
    def invert(self,s):

        s_list = list(s)
        for index in range(len(s_list)):
            if s_list[index] == "0":
                s_list[index] = "1"
            else:
                s_list[index] = "0"
        return "".join(s_list)
    def reverseBinary(self,s):
        s_list = list(s)
        left = 0
        right = len(s_list)-1
        while left < right:
            s_list[left],s_list[right] = s_list[right],s_list[left]
            left +=1
            right -=1
        return ''.join(s_list)
    @lru_cache
    def findBinaryString(self,n):
        if n==1:
            return "0"
        return self.findBinaryString(n-1) + "1" + self.reverseBinary(self.invert(self.findBinaryString(n-1)))

    def findKthBit(self, n: int, k: int) -> str:
        binary_string = self.findBinaryString(n)
        return binary_string[k-1]
        