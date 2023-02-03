n = int(input())
nums = [int(num) for num in input().split()]
has_odd = False
has_even = False
for num in nums:
    if num%2 ==0:
        has_even = True
    else:
        has_odd = True
if has_even and has_odd:
    print(*sorted(nums))
else:
    print(*nums)

