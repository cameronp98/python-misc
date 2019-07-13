def fib(n):
    a = 0
    b = 1
    
    for i in range(n):
        temp = a
        a = a + b
        b = temp

        yield a

    return a

