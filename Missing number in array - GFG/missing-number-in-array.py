#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        array_set = set(array)
        for num in range(1,n+1):
            if num not in array_set:
                return num


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends