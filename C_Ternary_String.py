from collections import defaultdict
T = int(input())
for t in range(T):
    nums = input()
    tarnary = defaultdict(int)
    left = 0
    right = 0
    min_sub = float('inf')
    for right in range(len(nums)):
        tarnary[nums[right]] +=1
        while len(tarnary) >= 3:
            min_sub = min(min_sub,right-left+1)
            tarnary[nums[left]] -=1
            if tarnary[nums[left]]  == 0:
                del tarnary[nums[left]] 
            left +=1
    if min_sub == float("inf"):
        print(0)
    else:
        print(min_sub)
            

        


        
        
        
        

