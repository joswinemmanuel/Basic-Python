day_num=int(input("Enter the day number from (1-7) : "))

"""if day_num==1:
    print("MONDAY")
elif day_num==2:
    print("TUESDAY")
elif day_num==3:
    print("WEDNESDAY")
elif day_num==4:
    print("THURSDAY")
elif day_num==5:
    print("FRIDAY")
elif day_num==6:
    print("SATURDAY")
elif day_num==7:
    print("SUNDAY")
else:
    print("INDALID day number")"""

match day_num:
    case 1:
        print("MONDAY")
    case 2:
        print("TUESDAY")
    case 3:
        print("WEDNESDAY")
    case 4:
        print("THURSDAY")
    case 5:
        print("FRIDAY")
    case 6:
        print("SATURDAY")
    case 7:
        print("SUNDAY")
    case _:
        print("INVALID day number")