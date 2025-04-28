# argument in function 
    #   there are four types of arguments 
    #    1.default  2.keyword 3. variable lengh  4.required arguments

#1. default argument 
def add(a=4,b=6):
    print(a+b)
add()
add(2,5)
 # here it ignors the default value
add(5)
  #a=5,b=default value
add(b=6)
#similar 

#2.keyword  argument 
add(b=9,a=8)
    #if pass argument in this manner thebn we no need to wary about the order

#3.requred argument
def add1(a,b=0):
    print(a+b)

add1(5)
 # a ir required argument which is needed 

# 4.variable lenght argument 
def add2(*num):
    sum=0
    for i in num:
        sum=sum+i
    return sum


sum1=add2(4,5,6)
print("average is:", sum1)
sum1=add2(4,5,6,56)
print("average is:", sum1)

# for dictionary
def name(**name):
    print("hello,",name["fname"],name["mname"],name["lname"])

name(mname="buchanan",lname="barnes",fname="james")