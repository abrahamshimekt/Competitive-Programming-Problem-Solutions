class Solution:

    def __init__(self, rects: List[List[int]]):
        w = 0
        self.rects = rects
        self.probability =[]
        self.indexes = []
        for i in range(len(self.rects)):
            self.indexes.append(i)
            w += (self.rects[i][2]-self.rects[i][0] +1)*(self.rects[i][3]-self.rects[i][1] +1)
        for i in range(len(self.rects)):
            self.probability.append((self.rects[i][2]-self.rects[i][0] +1)*(self.rects[i][3]-self.rects[i][1] +1)/w)
    def pick(self) -> List[int]:
        index = random.choices(self.indexes,weights = self.probability,k=1)[-1]
        x1,y1,x2,y2 = self.rects[index]
        return [random.randint(x1,x2),random.randint(y1,y2)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()