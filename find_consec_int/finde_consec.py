class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k  = k
        self.size = 0
        

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.size +=1
            if self.size >= self.k:
                return True
            return False
        else:
            self.size = 0
            return False

                
       

        

        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)