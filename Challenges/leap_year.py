# Write a program that find if a given year is leap year or not.
# This is how you find out if the year is leap year or not:
# -> On every year that is evenly divisible by 4
# --> except every year that is evenly divisible by 100
# ---> unless the year is also evenly divisible by 400

###############################################
# my try
############

chosen_year = int(input("Enter a fucking year: "))

if chosen_year % 4 == 0:
    if chosen_year % 100 == 0:
        if chosen_year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a Leap year!")
    else:
        print("Leap Year")
else:
    print("Not a Leap year!")

