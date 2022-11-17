class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = [num]
        num = list(f"{num}")
        for i in range(len(num)):
            if num[i] == "9":
                num[i] = "6"
                nums.append(''.join(num))
                num[i] = "9"
            else:
                num[i] = "9"
                nums.append(''.join(num))
                num[i] = "6"
        maxNum = 0
        for x in nums:
            if int(x) > maxNum:
                maxNum = int(x)
        return maxNum
            