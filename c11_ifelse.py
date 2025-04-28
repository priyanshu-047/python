# if else condition 

# 1.syntax of if else 
a=int(input("enter your age :"))
if(a>18):
    print("can do")
else:
    print("can't do")

#note the space in print statment called indentation 

# 2. elif use for multiple conition 
if(a>18):
    print("i am of 18")
elif(a>15):
    print("i am of 15")
else:
    print("smaller ")

# 3.nested if 
if(a<50):
    print("can be enter ")
    if(a<35):
        print("under age")