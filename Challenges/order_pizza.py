# Write a pizza order program where based on customer's choices
# calculate the costs of the order.


def menu():
    print("""
    S-> Small Pizza: $15
    M-> Medium Pizza: $20
    L-> Large Pizza: $25
    
    Pepperoni for small Pizza: +$2
    Pepperoni for Medium or Large Pizza: +$3
    
    Extra cheese for any size pizza: +$1
    """)


def main():
    total_cost = 0
    menu()
    order_size = input("Size: ").lower()
    pepperoni = input("Add pepperoni? ").lower()
    cheese = input("Extra cheese? ").lower()

    if cheese == "y":
        total_cost += 1

    if order_size == "s":
        total_cost += 15
        if pepperoni == "y":
            total_cost += 2
    elif order_size == "m":
        total_cost += 20
        if pepperoni == "y":
            total_cost += 3
    elif order_size == "l":
        total_cost += 25
        if pepperoni == "y":
            total_cost += 3
    else:
        print("Please enter choose either s, m, or l.")

    # Display the final bill
    print(f"Your final bill is: ${total_cost}.")


main()
