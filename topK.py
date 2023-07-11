from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    
        counter = Counter(nums)
        elements = list(counter.keys())

        def partition(left, right):
            pivot_freq = counter[elements[right]]
            i = left - 1
            
            for j in range(left, right):
                if counter[elements[j]] >= pivot_freq:
                    i += 1
                    elements[i], elements[j] = elements[j], elements[i]
            
            elements[i + 1], elements[right] = elements[right], elements[i + 1]
            return i + 1

        def quicksort(left, right):
            if left < right:
                pivot_index = partition(left, right)
                if pivot_index == k - 1:
                    return
                elif pivot_index > k - 1:
                    quicksort(left, pivot_index - 1)
                else:
                    quicksort(pivot_index + 1, right)
        
        quicksort(0, len(elements) - 1)
        return elements[:k]


        

        
        
