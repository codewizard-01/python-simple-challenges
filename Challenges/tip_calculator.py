# Build a tip calculator which looks something like this:
#################################
# Welcome to the tip calculator.
# What was the total bill? 124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93

###################################################
# This challenges is one Angela's course challenges.


#####################
# my code
####################

# Greeting and user inputs
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
num_ppl = float(input("How many people to split the bill? "))

# calculations
tip = bill * percentage
total_bill = bill + tip
each_ppl_pay = total_bill / num_ppl

# Display the final result
print(f"Each person should pay: ${round(each_ppl_pay, 2)}")


#######################
# Yours
#######################