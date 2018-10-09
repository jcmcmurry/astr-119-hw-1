import numpy as np  # numpy used everywhere apparently


def main():
    i = 0  # define int i initially at 0
    n = 10  # define int n initially at 10
    x = 119.0  # float x with value 119

    # we use numpy to declare arrays with ease

    y = np.zeros(n, dtype=float)  # declares n zeros

    # we can iterate through the elements of y by passing an index

    for i in range(n):  # i in range [0, n-1]
        y[i] = 2.0 * float(i) + 1.  # set y = 2i + 1

    # we can also simply iterate through an array
    for y_element in y:
        print(y_element)


# executes main function
if __name__ == "__main__":
    main()