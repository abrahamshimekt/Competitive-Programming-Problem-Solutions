class BrowserHistory:
    """
    stack = ["leetcode.com","google.com","facebook.com","linkedin.com"
    ]
    tempstack = ["youtube.com"]
    """

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.tempStack = []
        

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.tempStack = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.stack)>1:
            self.tempStack.append(self.stack.pop())
            steps -=1
        return self.stack[-1] 

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.tempStack) >0 :
            self.stack.append(self.tempStack.pop())
            steps -=1
        return self.stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)