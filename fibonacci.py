def fib(n):
        # fibArray = [0,1]
        # if n <= 0:
        #     return
        # elif n<=len(fibArray):
        #     return fibArray[n-1]
        # else:
        #     temp = fib(n-1 ) + fib(n -2)
        #     fibArray.append(temp)
        #     return temp
        if n ==0:
            return 0
        if n == 1:
            return 1
        return fib(n-1) + fib(n-2)
    