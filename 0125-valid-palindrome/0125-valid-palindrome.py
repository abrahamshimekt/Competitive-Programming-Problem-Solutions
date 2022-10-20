class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        aplpabets = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,
                 "j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,
                  "s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
                    "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        extracted_string = ""
        for c in s:
            if c.lower() in aplpabets:
                extracted_string += c.lower()
        i = 0
        j = len(extracted_string)-1
        while i < j:
            if extracted_string[i] != extracted_string[j]:
                return False
            i +=1
            j -=1
        return True