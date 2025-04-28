#  list 

# 1. syntax

nums = [89,90,98]
print(nums)
# 2. indexed valued 
print(nums[0])
# list are the order collection of data item  

lis = ["priyanshu ",2203630130020,True]
print(lis)
print(lis[2])

# 3. negative indexing in list 
print(lis[-1])
print(lis[len(lis)-1])
print(lis[2])
    #   above all are equals in above 

#4. searching value in the list
if True in lis :
    print("yes")
else:
    print("No")
    #    in key word find the value in the list

if "priyanshu " in lis :
    print("yes")
else:
    print("No")
    #    in key word find the value in the list
    
# 5. find some thing in the string 
v = "sohan"
if "s" in v:
    print("yes")

# 6. 
print(lis[:])
print(lis[1:])

# 7. jump statment 
print(lis[0::2])
    #   print(n:m:k) first it slice the string in n to m 
    #  it jums by n-1 that is 1 
    #    it print by ignoring one by one 

#  note out of index not for the lis 
print(lis[0:100])

# operation 
lis =[ i*i for i in range(4)]
print(lis)
    #    list first evalut the value then it make it element of its list

lis =[i*i for i in range(10) if i%2==0]
print(lis)

