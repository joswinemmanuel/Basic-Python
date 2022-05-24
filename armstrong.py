number=input("Enter the number : ")
sum=0
for i in number:
    sum+=int(i)**len(number)
if sum==int(number):
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is not an armstrong number")
    