def countingValleys(steps, path):
    height = 0
    countValley = 0
    for i in range(steps):
        if path[i] == "U":
            height +=1
            if height ==0:
                countValley +=1
        else:
            height -=1
    return countValley