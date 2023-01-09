class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.value_count = 0
       
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.value_count +=1
            if self.value_count >= self.k:
                return True
        else:
            self.value_count = 0
        return False
        
        
            
        
                
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)