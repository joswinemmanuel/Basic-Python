def fact(n):
    mul=1
    for i in range(1,n+1):
        mul*=i
    return mul

number=input("Enter the number : ")
sum=0
for i in number:
    sum+=fact(int(i))
if sum==int(number):
    print(f"{number} is a strong number")
else:
    print(f"{number} is not a strong number")