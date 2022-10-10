class Solution:
    def myAtoi(self, s: str) -> int:
        nums_dic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        num =" "
        s = s.strip()
        if len(s) == 0 or s== "+" or s=="-":
            return 0
        
        for i in range(len(s)):
            if (s[i] == "-" or  s[i] == "+") and i==0 :
                if s[i + 1] in nums_dic:
                    num += s[i]
            elif s[i] in nums_dic:
                num +=s[i]
            else:
                break
        if num == " "  :
            return 0
        elif int(num) <= -1*pow(2,31):
            return -1*pow(2,31)
        elif int(num) >= pow(2,31) -1:
            return pow(2,31) -1
        else:
            return int(num)
                