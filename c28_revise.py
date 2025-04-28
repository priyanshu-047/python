# list 
# create the list 
    #  method 1
list1=[]

    #method 2
list1=list()

    #method 3
list2=list("abcd")
print(list2)
name="priyanshu singh"

l=list(name)
print(l)

l1=list((1,2,3,4,5,6,7,8,9,0))
print(l1)
l1.reverse()
print(l1)

# methods
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

del l1[0]
print(l1)


# operation
lo=[x for x in range(10) if x%2==0]
print(lo)
lo1=[x for x in range(10) if x%3==0]
lo2=lo+lo1
print(lo2)
