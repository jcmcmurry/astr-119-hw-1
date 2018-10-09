#python exceptions let you deal with unexpected results

try:
    print(a)    #throws an exception since there was no 'a' defined
except:
    print("a is not defined")

#there are specific errors to help with cases
try:
    print(a)    #this will throw exception since a not defined
except NameError:
    print("a still ain't defined")
except:
    print("not sure WHAT you did, but you don' goofed somewhere")

#this printing of a will break the program, and show up as an
# actual error since a is not defined and the print is not in a try
print(a)