#Here user inputs a number of choice to determine if it is negative or positive or zero
number = float(input("Enter Number of your choice:   ")) #using float so that it covers both integer and decimal numbers.
if number > 0:
        print(" The number is positive ")
elif number == 0:
        print(" The number is 0 ")
else:
    print(" The number is negative ")