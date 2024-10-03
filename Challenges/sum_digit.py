# my solution
number = int(input("Number: "))
number_str = str(number)
accumulator = 0
for i in number_str:
    accumulator += int(i)

print(accumulator)