def flagStone():
    nums = input()
    nNums = nums.split()
    for i in range(len(nNums)):
        nNums[i] = int(nNums[i])
    if nNums[0]% nNums[2] > 0:
        nNums[0] = nNums[0]//nNums[2] +1
    else:
        nNums[0] = nNums[0]//nNums[2]
    if nNums[1]%nNums[2] > 0:
        nNums[1] = nNums[1]//nNums[2] +1
    else:
        nNums[1] = nNums[1]//nNums[2]
    return nNums[0] * nNums[1]
print(flagStone())

