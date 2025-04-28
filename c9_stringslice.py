#1. tacking some specific charecter  of the string--------------->
name = "mango"
print(name[0:5])
        #  here it prints (0-4) or( strart to n-1) indexted charecter
        #  including 0  but not 4
print(name[:5])
        #here it is same as the uper python autometicaly make 0 to starting 
print(name[3:4])
print(name[:])
        #this print the hole string start with zero and end with the lenght 

#2. finding lenth of the functon-----------------------------------> 
print(len(name))
     #len function returns the lenth of the string 


#3. negative slicing --------------------------------------------->
print(name[0:-2])
             # python read as print(name[0:len(string)-2])
print(name[-1:-3])
           # printing nothing same concept as the above
print(name[-3:-1])

#quize
mn = "harry"
print(len(mn))
print(mn[-4:-2])