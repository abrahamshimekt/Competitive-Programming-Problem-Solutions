class Solution:
    def detonate(self,bomb):
        stack = [bomb]
        detonated = {bomb}
      
        numberOfDetonatedBombs = 0
        while stack:
            currBomb = stack.pop()
            numberOfDetonatedBombs += 1
            for b in self.bombsInRange[currBomb]:
                if b not in detonated:
                    detonated.add(b)
                    stack.append(b)
        return numberOfDetonatedBombs

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.bombsInRange = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                bomb_i = bombs[i]
                bomb_j = bombs[j]
                distance_between = ((bomb_j[0]-bomb_i[0])**2 + (bomb_j[1]-bomb_i[1])**2)**0.5
                if distance_between <= bomb_i[2] and i != j:
                    self.bombsInRange[i].append(j)
       
        maxDetonation = 0
        for bomb in range(len(bombs)):
            maxDetonation = max(maxDetonation,self.detonate(bomb))
        return maxDetonation

        
