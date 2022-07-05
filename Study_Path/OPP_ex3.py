print(isinstance(42, int))

# int is a 'class' and 42 is an 'instance' of the class int

print(issubclass(bool, int))

# bool is a 'subclass' of the 'class' int

print(issubclass(int, object))
print(issubclass(str, object))
print(issubclass(bool, object))

# technically, everything is a subclass of object
