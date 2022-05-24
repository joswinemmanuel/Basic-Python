# To print the first n fibonacci numbers

def fib_n(n):
    if n<=1:
        print(0)
        return
    a=0
    b=1
    for i in range(n):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
    print()

fib_n(0) # 0
fib_n(4) # 0 1 1 2
fib_n(6) # 0 1 1 2 3 5
