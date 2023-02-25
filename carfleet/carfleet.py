class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dists_times = []
        for index in range(len(position)):
            dists_times.append([position[index],(target-position[index])/speed[index]])
        dists_times.sort()
        stack = []
        for dist_time in dists_times:
            while stack and stack[-1][1]<= dist_time[1]:
                stack.pop()
            stack.append(dist_time)
        return len(stack) 
        
        