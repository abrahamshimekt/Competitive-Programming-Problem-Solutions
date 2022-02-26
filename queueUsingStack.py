class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = 0
    def push(self, x: int) -> None:
        self.s1.append(x)
        self.length +=1
        return None
        

    def pop(self) -> int:
        if self.s2:
            self.length -=1
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            if self.s2:
                self.length -=1
                return self.s2.pop()
    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            if self.s2:
                return self.s2[-1]
    def empty(self) -> bool:
        return not bool(self.length)