# one liner
def palindrome(n):
    return n[::-1]

# for loop (list,tuple) case
def palindrome_lst(n):
    lst=[]
    for i in range(len(n)-1,-1,-1):
        lst.append(n[i])
    return lst

# for loop (string) case
def palindrome_str(n):
    s=''
    for i in range(len(n)-1,-1,-1):
        s+=n[i]
    return s

# Examples
print(palindrome('apple')) # elppa
print(palindrome([1,2,3,4])) # [4,3,2,1]
print(palindrome_str('apple')) # elppa
print(palindrome_lst([1,2,3,4])) # [4,3,2,1]