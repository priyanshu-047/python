# tuplews are immutable but it can be change in following manner 
#1.first convert to the list and then to tuple
cont =("spain","italy","india","england","garmany")
temp=list(cont)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
cont=tuple(temp)
print(cont)

#2.count 
coun=cont.count("russia")
print(coun)

#3.index -----slicimg also occur
#4. len