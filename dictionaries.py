#define a dictionary data structure

#dictionaries have a " key : value " for the elements
ex_dict = {
    "class"         : "Astr 119",
    "prof"          : "Brant",
    "awesomeness"   : "meh",
    "mediocrity"    : 10
}
print(type(ex_dict))

#get a value via key
course = ex_dict["class"]
print(course)

#Cahnge a value via key
ex_dict["mediocrity"] -= 1 #decreases mediocrity by 1

#print the dictionary
print(ex_dict, '\n')


#print dictionary element by element
print("Here they are step by step:")
for x in ex_dict.keys():
    print(ex_dict[x])