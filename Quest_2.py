try:
    x = input("Enter first number: ")
    y = input("Enter second number: ")

    xFloat = float(x)
    yFloat = float(y)

    def greaterThan( xFloat, yFloat):
        if xFloat>yFloat :
            print("{0} is greater than {1}".format(xFloat, yFloat))

        elif yFloat>xFloat :
            print("{0} is greater than {1}".format(yFloat, xFloat))
        else:
            equal()

    def lesserThan (xFloat,yFloat):
        if xFloat < yFloat:
            print("{0} is lesser than {1}".format(xFloat, yFloat))

        elif yFloat < xFloat:
            print("{0} is lesser than {1}".format(yFloat, xFloat))
        else:
            equal()

    def equal():
        print("Both are equal")

    greaterThan(xFloat,yFloat)
    lesserThan(xFloat,yFloat)

except ValueError:
    print("Please enter a numeric value for comparison.")




