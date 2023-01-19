#User function Template for python3

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
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends