class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_part = nums1[:m]
        first = 0
        second = 0
        k = 0
        while first < m and second < n:
            if num1_part[first] <= nums2[second]:
                nums1[k] = num1_part[first]
                first +=1
            else:
                nums1[k] = nums2[second]
                second +=1
            k +=1
        while first < m:
            nums1[k] = num1_part[first]
            first +=1
            k +=1
        while second < n:
            nums1[k] = nums2[second]
            second +=1
            k +=1

            

            
            


        
            

                

        
        
                    