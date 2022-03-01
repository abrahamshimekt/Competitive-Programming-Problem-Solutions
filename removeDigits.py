class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k: 
            return "0"
        digits = list(num)
        stack = []

        while digits and k:
            if not stack:
                stack.append(digits.pop(0))
            else:
                msd = digits.pop(0)
                while k and stack and stack[-1] > msd:
                        stack.pop()
                        k -= 1
                stack.append(msd)

        while k:
            # digits is empty
            stack.pop()
            k-=1
        
        digits = stack + digits
        # remove leading 0s
        while digits and digits[0] == "0":
            digits.pop(0)
        
        return "0" if not digits else ''.join(digits)