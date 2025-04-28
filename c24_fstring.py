#string formating 
#1.formating aur filling
letter="hey i am {} and i am from {}"
country ="india"
name="priyanshu"

print(letter.format(name,country))

letter="hey i am {1} and i am from {0}"
country ="india"
name="priyanshu"
print(letter.format(name,country))

#2.fstring
print(f"hey i am {name} and i am from {country}")


#3.
txt="for only {price:.2f} dollars!"
print(txt.format(price=49.09999)) 
price=49.099999
txt=f"for only {price:.2f} dollars!"
print(txt)

#4. fstering can evalute and return as the string
print(f"{6*6}")

#5.if we want to print as it is 
print(f"hey i am {{name}} and i am from {{country}}")

