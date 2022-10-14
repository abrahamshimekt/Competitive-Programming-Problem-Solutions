class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if total//cost1 <1 and total//cost2 < 1:
            return 1
        num_pens = 0
        num_ways = 0
        while num_pens <= total//cost1:
            num_ways += (total - num_pens*cost1)//cost2 + 1
            num_pens +=1
        return num_ways
            