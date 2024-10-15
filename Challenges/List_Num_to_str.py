# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

############################################################################################

def create_phone_number(n):
    country_code = ""
    first_part = ""
    second_part = ""
    counter = 0
    for i in n:
        if counter < 3:
            country_code += str(i)
            counter += 1
        elif counter < 6:
            first_part += str(i)
            counter += 1
        else:
            second_part += str(i)
            counter += 1

    return f"({country_code}) {first_part}-{second_part}"


# Display the result
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
