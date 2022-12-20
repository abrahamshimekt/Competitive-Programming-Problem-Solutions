 def multiply(self, num1: str, num2: str) -> str:
        nums = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        r1 = 0
        r2 = 0
        for k in num1:
            r1 = r1*10 + nums[k]
        for n in num2:
            r2 = r2*10 + nums[n]
        return str(r1*r2)