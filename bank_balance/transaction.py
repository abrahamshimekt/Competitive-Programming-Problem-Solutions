class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.length = len(self.balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.length and 1 <= account2 <= self.length:
            if self.balance[account1-1] < money:
                return False
            else:
                self.balance[account2-1] += money
                self.balance[account1-1] -= money
                return True 

        else:
            return False 

        

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.length :
            self.balance[account-1]  += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.length :
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
            else:
                return False
        else:
            return False

            