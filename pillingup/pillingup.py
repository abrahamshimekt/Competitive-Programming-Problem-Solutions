T = int(input())
for i in range(T):

    max_cub = float("inf")
    n = int(input())
    blocks = input().split()
    l,r = 0,n-1
    canpile = True

    while l <=r:

        if int(blocks[r]) >= int(blocks[l]):

            curr_block = int(blocks[r])
            
            if curr_block > max_cub:
                canpile = False
                break

            else:
                max_cub = curr_block
                r -=1

        elif int(blocks[l]) >= int(blocks[r]):

            curr_block = int(blocks[l])

            if curr_block > max_cub:
                canpile = False
                break

            else:
                max_cub = curr_block
                l +=1

    if canpile:
        print("Yes")  

    else:
        print("No")