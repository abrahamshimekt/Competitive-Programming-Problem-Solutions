class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.big = big
        self.medium = medium 
        self.small  = small
        
    def addCar(self, carType: int) -> bool:

        if carType == 1:
            
            if self.big > 0:
                # while adding each new car of type big to the slot
                # the number of slots will decrease
                self.big -=1
                return True

            else: 
                return False

        elif carType == 2:

            if self.medium >0:
                # while adding each new car of type medium to the slot
                # the number of slots will decrease
                self.medium -=1
                return True

            else:
                return False

        else:

            if self.small >0:
                # while adding each new car of type small to the slot
                # the number of slots will decrease
                self.small -=1
                return True

            else:
                return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)