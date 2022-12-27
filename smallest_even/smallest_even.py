def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,3):
            if i*n %2 ==0:
                return i*n