print("Guess the number between 1 and 10, only 3 chances")
ans=5
for i in range(1,4):
    if int(input(f"Guess number {i} : "))==ans:
        print("You WON")
        break
else:
    print("You LOST")