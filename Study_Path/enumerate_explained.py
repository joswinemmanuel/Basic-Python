colors = ['red', 'green', 'orange']

print(list(enumerate(colors)))

for i,j in enumerate(colors):
    print(i,j)

""" enumerate gives a tuple of the index and element for each element """