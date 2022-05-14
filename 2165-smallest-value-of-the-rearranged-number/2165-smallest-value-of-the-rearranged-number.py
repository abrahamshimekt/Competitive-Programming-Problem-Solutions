class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        elif num >0:
            num_list = [x for x in str(num)]
            num_sorted = sorted(num_list)
            if num_sorted[0] =="0":
                for i in range(1,len(num_sorted)):
                    if num_sorted[i] > num_sorted[0]:
                        num_sorted[0],num_sorted[i] = num_sorted[i],num_sorted[0]
                        return int("".join(num_sorted))
            else:
                 return int("".join(num_sorted))
        else: 
            num_list = [x for x in str(-1*num)]
            num_sorted = sorted(num_list,reverse= True)
            if num_sorted[0] =="0":
                 for i in range(1,len(num_sorted)):
                    if num_sorted[i] > num_sorted[0]:
                        num_sorted[0],num_sorted[i] = num_sorted[i],num_sorted[0]
                        return -1*int("".join(num_sorted))
            else:
                 return -1*int("".join(num_sorted))
        
        
    
            
        