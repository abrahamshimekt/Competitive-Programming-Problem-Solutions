class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        num1 = num1.split('+')
        num2 = num2.split("+")

        # if we have given two complex numbers (a+bi) and (x+yi)
        # then their product will be ax-by + (ay+bx)*i

        real_part = int(num1[0])*int(num2[0]) - int(num1[1][:-1]) * int(num2[1][:-1])
        imaginary_part = int(num1[0])*int(num2[1][:-1]) + int(num1[1][:-1])*int(num2[0])

        product = f'{real_part}+{imaginary_part}i'
        
        return product