#include numpy library
import numpy as np

#define main() function
def main():

    i = 0      #declare I, initialize to 0
    x = 119.0  #declare a float x

    for i in range(120): #loop i from 0 to 119 inclusively
        if((i%2)==0): #if i is even
            x += 3    #adds 3 to x
        else:
            x -= 5    #subtracts 5 from x
    s = "%3.2e"%x # % means number, 3 is total numbers shown,
                  # 2 is num of decimal places, and e makes sci notation
                  # this makes a string s containing the value of
                  #x in sci notation with 2 decimals showing

    print(s)    #prints s to the screen

#getting rid of indent makes us exit the function, in this case, main()

if __name__== "__main__": #call main
    main()  #runs main function