from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inheritance = defaultdict(list)
        self.inheritance[self.kingName] = []
        self.deads = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.deads.add(name)

    def getInheritanceOrder(self) -> List[str]:

        stack = [self.kingName]
        currOrders = []

        while stack:
            name = stack.pop()
            if name not in self.deads:
                currOrders.append(name)
            for n in self.inheritance[name][::-1]:
                stack.append(n)
        return currOrders


        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
