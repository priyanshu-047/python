def admin():
    print("<---------------wellcome to admin mode-------------->")
    print("<---------------enter your id and password-------------->")
    id=int(input("enter your id number :"))
    password=int(input("enter your password :"))
    if(password==123 and id==123):
          name=input("enter the name serching for :")
          if name in list:
              print("yes present \n")
          else:
              print("not present \n ")
    else:
         print("invalid account :")
         print("bostening again--------------------------->")
         main()
    print("bostening again--------------------------->")
    main()
   
   
   
   

def worker():
    print("<---------------wellcome to emploee mode-------------->")
    print("enter your name for adendence:")
    i=0
    n=input()
    list.append(n)
    i=i+1
    main()


def main():
    a="y"
    while(a=="y" or a=="Y"):
            print("enter your post:")
            b=int(input("if admin then enter 1:\notherwise press 2:"))
            if(b==1):
                 admin()
                 a=n
            elif(b==2):
                worker()
                a=n
            else:
                print("envalid! enter again")
print('<-------------------wellcom to offic-------------------->')
list=[]
main()

   