class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n-1
        first = m-1
        second = n-1

        while second > -1 and first > -1:
            if nums2[second] > nums1[first]:
                nums1[k] = nums2[second]
                second -=1
            else:
                nums1[k] = nums1[first]
                first -=1
            k -=1
        while second > -1:
            nums1[k] = nums2[second]
            second -=1
            k -=1
        
            

                

        
        
                    