import numpy as np
import sys

#define a function that returns a value
def expo(x):
    return np.exp(x) #return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
    for i in range (n): #i from 0 to n-1
        print(expo(float(i))) #call e^float(i)

#define a main function
def main():
    n= 10

    #check if a command line argument is provided
    if(len(sys.argv>1)):     #if we give len an array, it tells us how long the array is. argv is a
        n = int(sys.argv[1]) #if an argument is provided, use it as an int for n

    show_expo(n) #call expo subroutine

#run main function
if __name__ == "__main__":
    main()