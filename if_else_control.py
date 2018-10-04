#define a function
def flow_control(k):

    #define a string based an the value of k
    if(k==0):
        s= "Variable k = %d equals 0." % k
    elif(k==1):
        s= "Variable k = %d euqals 1." % k
    else:
        s = "Variable k = %d does not euqal 0 or 1." % k

    #print the variable
    print(s)

def main():

    i = 0

    #try flow control for 0, 1, or 2
    flow_control(i)
    i=1
    flow_control(i)
    i=2
    flow_control(i)

if __name__ == "__main__":
    main()