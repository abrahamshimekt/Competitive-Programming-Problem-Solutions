class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.arr = arr
        self.capacity = capacity
        self.length = length
    # write your code here
    
    def insertEnd(self, value):
        if self.capacity >= self.length:
            self.arr[self.length]  = value
            self.length +=1
        

    # write your code here
    
    def removeEnd(self):
        if self.length > 0:
            self.arr[self.length] = 0
            self.length -=1
    
    def insertMiddle(self, index, value):
    # write your code here, you need to shift elements after insertion
    
    def removeMiddle(self, index):
    # write your code here, you need to shift elements after removal
    
    def printArr(self):
    # write your code here