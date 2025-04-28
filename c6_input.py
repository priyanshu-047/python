#  python take input by input function --------------->

#1. simple input
print("enter")
a=input()
print(a) 

#2. input function always take all value as string also
b=input("enter your name :")
print(b)

#3.  input function only takes string 
c=input("ener the first number :")
d=input("enter the second number:")
print("sum is :",(c+d))

#4. so also use type coasting to convert the type 
e=input("ener the first number :")
f=input("enter the second number:")
print("sum is :",int(e)+int(f))