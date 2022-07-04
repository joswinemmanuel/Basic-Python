def hashable(value):
    try:
        print(type(value),"is hashable, has value is",hash(value),'\n')
    except:
        print(type(value),"is not hashable","\n")

hashable(5)
hashable(1.1)
hashable(0+5j)
hashable("a")
hashable(())
hashable([])
hashable(set())
hashable({})


