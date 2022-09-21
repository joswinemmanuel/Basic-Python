year = int(input("Enter the year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR")
        else:
            print("Not LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("Not LEAP YEAR")