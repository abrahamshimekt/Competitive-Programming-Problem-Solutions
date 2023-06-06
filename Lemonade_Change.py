class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        n = len(bills)
        for index in range(n):
            change = bills[index]-5

            if change//10 and change//10<= ten:
                ten -= change//10
                change %=10
            if change//5 and change//5 <= five:
                five -= change//5
                change %= 5
            if change != 0:
                return False

            
            if bills[index] == 10:
                ten +=1
            elif bills[index] == 5:
                five +=1
        return True
        

            
        
