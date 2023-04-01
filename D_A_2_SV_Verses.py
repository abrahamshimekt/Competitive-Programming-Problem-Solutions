def find_subarray(nums,k,n):
    left = 0
    curr_sum = 0
    sub_array= 0
    for right in range(n):
        curr_sum += nums[right]
        while curr_sum > k:
            curr_sum-= nums[left]
            left +=1
        sub_array += right-left+1
    return sub_array

n,a,b = map(int,input().split())
nums= list(map(int,input().split()))
atmostb,atmosta = find_subarray(nums,b,n),find_subarray(nums,a-1,n)
print(atmostb-atmosta)

    
