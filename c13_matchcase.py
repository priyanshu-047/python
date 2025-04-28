# match case is similer as switch case 
x=int(input("enter the value x "))

match x:
    case 1:
        print("case one ")
    case 2:
        print("case two")
    case _ if(x!=25):
        print("default case ")
    # default case can be more than one with if condition 
    case _ if(x!=20):
        print("it is 80")
   