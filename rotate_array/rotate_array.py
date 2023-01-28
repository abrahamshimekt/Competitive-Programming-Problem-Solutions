class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
       
        Do not return anything, modify nums in-place instead.
        """
        last_k = []
        first = []

        length = len(nums)
        k = k%length 
        # the naive and the most basic approach is to break down the array into two arrays and
        # added the rotated part first and the remaining lastly
        # the rotation of the array happens in k modulo by the length of the array
        # this approarch consums space with complexity big O of N and time complexity of O(N)

        for index in range(length):

            if index < length -k:
                first.append(nums[index])
            else:
                last_k.append(nums[index])


        index_k = 0

        while index_k < k:

            nums[index_k] = last_k[index_k]
            index_k +=1

        for index_ in range(length -k):
            nums[index_+ index_k] = first[index_]
        


        



        
        
       
            
        