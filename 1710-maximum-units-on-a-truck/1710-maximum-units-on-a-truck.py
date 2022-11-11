class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse = True)
        maxUnits = 0
        for boxType in boxTypes:
            if truckSize >0:
                if boxType[0] < truckSize:
                    maxUnits +=  boxType[0]*boxType[1]
                    truckSize -= boxType[0]
                else:
                    maxUnits +=  (truckSize)*boxType[1]
                    truckSize -= (truckSize)
            else:
                break
        return maxUnits
                
            