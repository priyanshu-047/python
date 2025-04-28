# pop8
# docstring define the function 

# 1. decleration 
def square(n):
    #  docstrings are describe here as comment but it not ignore by the compiler 
    '''takes a umber and 
    returns square of it '''
    print(n**2)

square(5)
# it can be access by __doc__
print(square.__doc__)

# 2. case second of docstring
def me():
    print("he")
    '''it never be doc 
     becouse it does not on the top '''
print(me.__doc__)
        #  hence doc is none 