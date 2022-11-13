class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for num in nums :
            num = f"{num}"
            mapped = ""
            for n in num:
                mapped += f"{mapping[int(n)]}"
            arr.append([int(num),int(mapped)])
        ans = sorted(arr,key=lambda x: x[1])
        n = len(ans)
        for i in range(n):
            ans[i] = ans[i][0]
        return ans
                