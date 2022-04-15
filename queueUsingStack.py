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
    
    
    
    class MyQueue:

    def __init__(self):
        self.stack1 =[]
        self.stack2 =[]

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return not self.stack1
