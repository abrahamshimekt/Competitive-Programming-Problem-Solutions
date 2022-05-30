class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output =[]
        for i in range(1,n+1):
            if i not in target:
                if i > target[-1]:
                    break
                output.append("Push")
                output.append("Pop")
            else:
                output.append("Push")
        return output
                