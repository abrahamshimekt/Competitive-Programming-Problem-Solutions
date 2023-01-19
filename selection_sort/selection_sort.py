class Solution: 
    def select(self, arr, i):
        min_num = float('inf')
        length = len(arr)
        pos = i
        for index in range(i,length):
            if arr[index] < min_num:
                min_num = arr[index]
                pos = index
        return min_num,pos
        
    
    def selectionSort(self, arr,n):
        for index in range(len(arr)):
            min_num,pos = self.select(arr,index)
            arr[index],arr[pos] = arr[pos],arr[index]
        return arr