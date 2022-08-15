''' Many arithmetic functions are naturally defined inductively '''
# FACTORIAL : n! = n x (n-1) x (n-2)! 
# MULTIPLICATION (repeated addition):
# 5 x 3 = 5 + 5 + 5 or 3 + 3 + 3 + 3 + 3


def mult(n, m):
    if m <= 1:
        return n
    return n + mult(n, m-1)

print(mult(5, 3))
