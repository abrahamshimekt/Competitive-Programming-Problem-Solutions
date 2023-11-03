class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target = target[::-1]
        ops = []
        num = 1
        while target:
            ops.append("Push")
            if num == target[-1]:
                target.pop()
            else:
                ops.append("Pop")
            num +=1
        return ops

            

        