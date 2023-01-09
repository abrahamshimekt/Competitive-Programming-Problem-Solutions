#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
	    
		p = K-1
		l = 0
		r = p
		if K >=N:
		    p = N-1
		    r = p
		while l < r :
		    arr[l],arr[r] = arr[r],arr[l]
		    l +=1
		    r -=1
		    if r <= l:
		        l = p+1
		        p += K
		        r = p
		        if p >=N:
		            p = N-1
		            r = p
		          
		    


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends