# using for loop
def fac(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f

# using recusion
def rec_fac(n):
    if n<=0:
        return 1
    else:
        return n*rec_fac(n-1) 

# Examples
print(fac(5)) # 120
print(rec_fac(5)) # 120

