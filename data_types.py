import numpy as np

#integers

i = 10
print(type(i))

a_i = np.zeros(i,dtype = int)
print(type(a_i))            #will return ndarray
print(type(a_i[0]))         #will return int64 (depending on computer)

#floats

x = 119.0
y = 1.19e2
z = np.zeros(i,dtype=float)

print(type(x))      #prints x's data type of float
print(type(y))      #prints y's data type also of float since it was put in sci notation
print(type(z))      #prints z's data type of ndarray
print(type(z[0]))   #prints z's 0th element's data type


#strings

s = "I am a string"

print(type(s))      #will say str

#Boolean

yes = True
no = False

print(type(yes))    #will return bool True
print(type(no))     #will return bool False

#List -- ordered and changeable

alpha_list = ["a", "b", "c"]    #list initialization
print(type(alpha_list))         #will say list
print(type(alpha_list[0]))      #will say string
alpha_list.append("d")          #adds an element to the list end
print(alpha_list)               #will print list

#Tuple -- ordered and unchangeable

beta_tuple = ("a", "b", "c")    #tuple initialization
print(type(beta_tuple))         #wil say tuple

try:
    beta_tuple[2]="d"           #will attempt to change the tuple which will get a type error
except TypeError:               #upon a type error, the direction sent would be sent down this tree
    print("Can't change elements in tuples!")
print(beta_tuple)               #prints the tuple


#Data Structures-- Arrays

x = [0.0, 3.0, 2.5, 3.7]   #define an array
print(type(x))                  #will print as list, but technically an array since it's numbers

#remove third element
x.pop(2)
print(x)

#add an element to the end
x.append(1.2)
print(x)

#creates a full independent copy with separate pointers, etc.
y = x.copy()
print(y)

#how many elements are 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))

#sort the list
y.sort()
print(y)

#reverse sorted list
y.reverse()
print(y)

#remove all elements from an array
y.clear()
print(y)