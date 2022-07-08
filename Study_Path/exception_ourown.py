class IncorrectValueError(Exception):
    def __init__(self, value):
        message = f"Got a bad value : {value}"
        super().__init__(message)

my_val = 999

if my_val < 1000:
    raise IncorrectValueError(my_val)