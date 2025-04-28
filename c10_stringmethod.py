# 1.concept of imutiblity
    #   string are imutible
name ="!priyanshu singh!!"
print(name)
name.upper()
print(name)
     #here the name is same as the older 
print(name.upper())
      #here it change by macking copy of it


# 2.lower case and upper case
print(name.upper())
print(name.lower())
    # these method returns new string 

# 3.removing unwanted symbols from string 
print(name.rstrip("!"))
            #it only strip the tells strips not of front 

# 4.replace
print(name.replace("n","Q"))
           #it replace all the occuring string with new value

# 5.split
print(name.split(" "))
         #it make the list (individual element of list) when it seen  passing value

# 6.capitalise
name="priyanshu SINgh!"
print(name.capitalize())
         #it convert first charecter to upper case and remainig to lower case

#7. center method
print(len(name))
print(name.center(50))
print(len(name.center(50)))
          #it make the string lenth of 50 by adding the space on front

# 8.count function 
print(name.count("h"))
      # cout the given string in the variable

#9. ends with
print(name.endswith("!"))
       # it returns bullean type data 
print(name.endswith("to",4,10))
        # this slice the string first and then check

# 10. find method
print(name.find("p"))
        # it returns indext of the first occurence of p in string
        #it return -1 if not found
# 11. index method 
print(name.index("p"))
        # same as find
        # but when item not found then it generate error(exeption)

# 12. isalnum method  
print(name.isalnum)
        #  it gives true if string only made up of the alpha-numeric charecters 

#13. isalpha method
# same as the isalum but it not include 0-9 numbers in string

# 14. islower method 
# 15. isprintable
     # it returns true if string have all printable charecter in string 
# 16. isspace method 
    #   returs true if string only have spaces 
# 17.istitle method
    # return true if all first letter have capitale
print(name.istitle)