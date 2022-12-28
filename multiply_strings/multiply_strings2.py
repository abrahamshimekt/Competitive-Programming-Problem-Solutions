def multiply(self, num1: str, num2: str) -> str:

        "since we cannot use the int function for casting,we need dictionary for matching"

        nums = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        num1_length = len(num1)-1
        num2_length = len(num2)-1

        first_num = 0
        second_num = 0
        
        # every number can be expressed mathematically as its tenth power place
        # for example let use take 123, this number has a maximum of 10**2 place of digits
        # so 123 can be expressed as 1*10**2 + 2*10*1 + 1*10**0 
        # to generalize let a = has n digits, then a can be expresse as
        #  a = a0*pow(10,n-1) + a1*pow(10,n-2)...an-1*pow(10,0)

        for number1 in num1:
            first_num += nums[number1]*pow(10,num1_length)
            num1_length -=1

        for number2 in num2:
            second_num+= nums[number2] *pow(10,num2_length)
            num2_length -=1 

        return str(first_num*second_num)