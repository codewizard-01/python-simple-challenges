# Write a program that get a number from a user and then sum all digits of that number together.

#####################
# my solution
####################

number = int(input("Number: "))
number_str = str(number)
accumulator = 0
for i in number_str:
    accumulator += int(i)

print(accumulator)


#######################
# Your solution  below
#######################