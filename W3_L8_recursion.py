''' Many arithmetic functions are naturally defined inductively '''
# FACTORIAL : n! = n x (n-1) x (n-2)! 
# MULTIPLICATION (repeated addition):
# m x 1 = m, m(n+1) = m + (mxn)


def mult(n, m):
    if m <= 1:
        return n
    return n + mult(n, m-1)

print(mult(5, 3))