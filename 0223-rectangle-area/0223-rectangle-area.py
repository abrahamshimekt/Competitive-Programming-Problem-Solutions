class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        xRange1 = [ax1,ax2]
        yRange1 = [ay1,ay2]
        xRange2 = [bx1,bx2]
        yRange2 = [by1,by2]
        intersectionXRange = [max(xRange1[0],xRange2[0]),min(xRange1[1],xRange2[1])]
        intersectionYRange = [max(yRange1[0],yRange2[0]),min(yRange1[1],yRange2[1])]
        rect1Area = (ax2-ax1)* (ay2-ay1)
        rect2Area = (bx2-bx1)*(by2-by1)
        intersectionArea = (intersectionXRange[1]-intersectionXRange[0])*(intersectionYRange[1]-intersectionYRange[0])
        if intersectionXRange[1]-intersectionXRange[0] <=0:                 
            return  rect1Area + rect2Area
        elif intersectionYRange[1]-intersectionYRange[0] <= 0:
            return  rect1Area + rect2Area
        return rect1Area + rect2Area-intersectionArea
        