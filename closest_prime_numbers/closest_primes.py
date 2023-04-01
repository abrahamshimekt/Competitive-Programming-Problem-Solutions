class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [num for num in range(2,right+1)]
        seive= 2
        while seive*seive <= right:
            if nums[seive-2] == 0:
                seive +=1
            else:
                d = seive*seive
                while d <=right:
                    nums[d-2] = 0
                    d +=seive
                seive +=1

        primes = []

        for index in range(len(nums)):
            if nums[index] >=left:
                prime = nums[index]
                primes.append(prime)
        
        minimum_pairs = [0,1000001]

        ptr1= 0
        ptr2 = 1

        while ptr2 < len(primes):
            nums1 = primes[ptr1]
            nums2 = primes[ptr2]
            if nums2 - nums1 < minimum_pairs[1]-minimum_pairs[0]:
                minimum_pairs = [nums1,nums2] 
            ptr1 += 1
            ptr2 += 1
            
        return [-1,-1] if minimum_pairs[1] == 1000001 else minimum_pairs