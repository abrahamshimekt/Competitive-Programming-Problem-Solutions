class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # bucket1 =[]
        # bucket2 =[]
        #maxPick = 0
        #starting = 0
        #ending  = 0
        #while starting < len(fruits) and ending < len(fruits): strat from the the zero index
        #let us fill the buckets starting the starting fruit type
        #if  bucket1 ==[]:
        #bucket.append()
        # increase ending by one 
        #else bucket2 ==[]
        #bucket2.append()
        #increase ending by 1
        #else check the fruit type fit in one of the buckets by cheking if the type is in the bucket
        # then in crease the value ending until u get a type not fit in any of the buckekst. the assign the diff of ending - starting to the maxPick  if it is greater than the previouse one. then in crease the start by one and make the endign the the startin a the same pos .go until ending == n -1
        # [1,2,1]
        f = Counter(fruits)
        maxpick = 0
        if len(f) ==1:
            return f[fruits[0]]
        elif len(f) ==2:
            for key in f:
                maxpick +=f[key]
            return maxpick
        else:
            basket1 = []
            basket2 =[]
            i = 0
            j = 0
            while i <len(fruits) and j < len(fruits):
                if basket1 ==[]:
                    basket1.append(fruits[j])
                    if j == len(fruits) -1:
                        if  maxpick < j-i +1:
                            maxpick =  j-i +1
                        i +=1
                        j = i
                        basket1.pop()
                    else:
                        j +=1
                elif fruits[j] in basket1:
                    if j == len(fruits) -1:
                        if  maxpick < j-i +1:
                            maxpick =  j-i +1
                        i +=1
                        j = i
                        basket1.pop()
                    else:
                        j +=1
                elif basket2 ==[]:
                    basket2.append(fruits[j])
                    if j == len(fruits) -1:
                        if  maxpick < j-i +1:
                            maxpick =  j-i +1
                        i +=1
                        j = i
                        basket1.pop()
                        basket2.pop()
                    else:
                        j +=1

                elif fruits[j] in basket2:
                    if j == len(fruits) -1:
                        if  maxpick < j-i +1:
                            maxpick =  j-i +1
                        i +=1
                        j = i
                        basket1.pop()
                        basket2.pop()
                    else:
                        j +=1
                else:
                    if  maxpick < j-i :
                        maxpick =  j-i
                    i +=1
                    j = i
                    basket1.pop()
                    basket2.pop()
            return maxpick