class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # I can use two pointers 
        # take example [-4,-1,0,3,10]
        # when i = 0, j = 4
        # output = []
        # compare is square(ith element) >= squeare(jth element)?if:
         # output.append(the squere of the ith element) increment i by one
        # else if the square of the jth element is greater than square of the ith element 
        # ouput.appned the square jth element and decreament j by 1
        # output = [100]
        # loop until j >=i                       
        # output = [100]
        # output = [100,16]
        # output = [100,16,9]
        # output = [100,16,9,1]
        # output = [100,16,9,1,0]
        # [-2,-1,0,1,2]
        #output = [4,4,1,1]
        output = []
        i ,j = 0,len(nums)-1
        while j >= i:
            if (nums[i])**2 >= (nums[j])**2:
                output.append((nums[i])**2)
                i +=1
            else:
                output.append((nums[j])**2)
                j -=1
        return output[::-1]
        