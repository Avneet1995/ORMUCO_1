
x=list()                     # first line
y=list()                     # second line

def manual_input():
    try:
        for i in range(2):
            z = int(input("Enter co-ordinates of line 1: "))
            x.append(z)
            x.sort()                  # sorts in ascending order

        for i in range(2):
            z = int(input("Enter co-ordinates of line 2: "))
            y.append(z)
            y.sort()
    except ValueError:                # exception handling for wrong data type
        print("Please enter an integer.")

def overlap_check():
    flag = 0                            # counter to check over lap
    for i in range(2):
        if (x[i] > y[0]) & (x[i] < y[1]):
            flag = 1

        elif (x[0] == y[0]) & (x[1] == y[1]):  # for same co-ordinates
            flag = 1

    if (flag == 0):
        print("No over lapping!")
    elif (flag == 1):
        print("Both lines over lap!")

manual_input()
overlap_check()








