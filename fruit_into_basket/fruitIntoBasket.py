class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
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