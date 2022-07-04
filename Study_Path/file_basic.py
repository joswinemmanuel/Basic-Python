with open("new_file.txt","w") as f:
    f.write("New txt file made using python")


with open("new_file.txt","r") as f:
    print(f.read())