class Solution:
    binary_string = '0'
    def invert(self,s):

        s_list = list(s)
        for index in range(len(s_list)):
            if s_list[index] == "0":
                s_list[index] = "1"
            else:
                s_list[index] = "0"
        return "".join(s_list)

    def reverseBinary(self,s):
        return s[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return self.binary_string[k-1]
        self.binary_string += "1"+ self.reverseBinary(self.invert(self.binary_string))
        
        return self.findKthBit(n-1,k)
        