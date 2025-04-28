# loop in python 
#  nexted loop 
# ittreable object 
#         1. list  2. string  3

#  for loop
# 1. for string 
name = "priyanshu singh "
for i in name :
    print(i)
    if i=="y":
        print("this is special key in the namer :",i)

color = [ "red" ,"green" ,"blue",'yellow']
for i in color :
    print(i)
 
 #2. range function in for loop
    
    # range with sing parameter 
for k in range(5):
    #    it gives for(k=0;k<=4;k++)
    print(k+1)
       
    #  range with double parameter 
for k in range(1,5):
    print(k)
        #    it goes to 4  that is range(i,n-1)

for k in range(12,23,4):
    print(k)

# while loop
i = 0
while(i<3):
    print(i)
    i=i+1

# while with else condition 
while(i<-1):
    print("hello")
    i=i+1
else:
    print("condition false")
    # when the the while loop does not run then this else condion exixute

#  python does not have do while loop
    # but it can be create bu rapping the while loop with break condition 
    #  which works similar as do while loop

#  note -> concept of do will loop by the while loop
i=0
while True:
    print(i)
    i = i+1
    if(i==5):
        break
