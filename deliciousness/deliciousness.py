def countPairs(self, deliciousness: List[int]) -> int:
        powers_of_2 = {}
        for power in range(0,22):
            powers_of_2[pow(2,power)]= 1

        d_freq = {}
        for meal in deliciousness:
            if meal not in d_freq:
                d_freq[meal] = 1
            else:
                d_freq[meal] +=1

        modulo = pow(10,9) +7
        pairs = 0
        lookup = {}
        
        for meal_ in d_freq:
            for power_of_2 in powers_of_2:
                if power_of_2 -meal_ in d_freq and meal_ ==power_of_2 -meal_:
                    pairs += ((d_freq[meal_]*(d_freq[meal_]-1))//2)
                elif power_of_2 -meal_ in d_freq and power_of_2 -meal_ not in lookup:
                    pairs += (d_freq[meal_]*d_freq[power_of_2 -meal_])
            lookup[meal_] =1
        return pairs %modulo