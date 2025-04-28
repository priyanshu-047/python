# recursion in python 

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
       return  fact(n-1)*n
    

print(fact(4))

def feb(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return feb(n-1)+feb(n-2)
    
print(feb(9))


