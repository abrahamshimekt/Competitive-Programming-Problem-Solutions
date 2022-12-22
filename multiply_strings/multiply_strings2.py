def multiply(self, num1: str, num2: str) -> str:
        nums = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        n = len(num1)-1
        m = len(num2)-1
        p1 = 0
        p2 = 0
        for n1 in num1:
            p1 += nums[n1]*pow(10,n)
            n -=1
        for n2 in num2:
            p2 += nums[n2] *pow(10,m)
            m -=1 
        return str(p1*p2)