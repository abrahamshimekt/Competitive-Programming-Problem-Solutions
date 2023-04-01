def findwinner(indexes,nums,k):
    winners = []
    for i in range(0,len(indexes),2):
       if i + 1 < len(indexes):
            if nums[indexes[i]] > nums[indexes[i+1]] and nums[indexes[i]]-nums[indexes[i+1]] > k:
                winners.append(indexes[i])
               
            elif nums[indexes[i+1]] > nums[indexes[i]] and nums[indexes[i+1]]-nums[indexes[i]] > k:
                winners.append(indexes[i+1])
                
            else:
                winners.append(indexes[i])
                winners.append(indexes[i+1])
       else:
           winners.append(indexes[i])

    if winners == indexes:
        return winners
    return findwinner(winners,nums,k)

n,k = map(int,input().split())
nums = list(map(int,input().split()))

indexes = [i for i in range(2**n)]
res = findwinner(indexes,nums,k)
for x in res:
    print(x+1,end=' ')
