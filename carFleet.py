from ast import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target-p)/s for p, s in sorted(zip(position, speed))]
        result, curr = 0, 0
        for t in reversed(times):
            if t > curr:
                result += 1
                curr = t
        return result