def multiply(self, num1: str, num2: str) -> str:

        nums = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

        first_num = 0
        second_num = 0

        # a number can be expressed as for example 
        # 124 = (0*10 + 1), ((0*10 + 1)*10 + 2 ), (((0*10 + 1)*10 + 2 )*10)+4  
        # so the ith term is 10 times the i-1 term plus the current digit
        
        for number1 in num1:
            first_num = first_num*10 + nums[number1]

        for number2 in num2:
            second_num = second_num*10 + nums[number2]

        return str(first_num*second_num)