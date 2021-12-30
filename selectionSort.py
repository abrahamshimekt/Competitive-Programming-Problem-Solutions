#https://auth.geeksforgeeks.org/user/shimektabraham/practice/#problem-solved-div
class Solution: 
    def select(self, arr, i):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                i = j
        return i
    
    def selectionSort(self, arr,n):
        for e in range(n):
            k = self.select(arr,e)
            arr[e],arr[k] = arr[k],arr[e]
        return arr