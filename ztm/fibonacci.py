def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a 
        a = b
        b = temp + b
        
        

f = fib(10)
for i in f:
    print(i)