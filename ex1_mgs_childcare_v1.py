""" MGS ChildCare v1 - keep track of children in child care
Created by Joseph Wong
24/02/2022
"""


# Drop Off Function
def drop_off():
    name = input("Enter the name of child to check-in: ")
    roll.append(name)
    print(f"{name} has been added to the list.")


# Pick Up Function
def pick_up():
    name = input("Enter the name of child to check-out: ")
    if name in roll:
        roll.remove(name)
        print(f"{name} has been removed from the roll.")
    else:
        print(f"Error! {name} could not be found in the roll. Please check.")


# Calculate Cost Function
def calc_cost():
    global HOURLY_RATE
    # from collections import namedtuple
    # constants = namedtuple("const", "HOURLY_RATE")
    # consts = constants(12)
    hours = float(input("Enter the number of hours to charge: "))
    num_children = len(roll)
    total_cost = hours * HOURLY_RATE * num_children
    print(f"It costs ${total_cost} for "
          f"looking after {num_children} children for {hours} hours.")


# Print Roll Function
def print_roll():
    print("This is the current roll list: ")
    for child in roll:
        print(child)


# Main Routine
HOURLY_RATE = 12
roll = []
choice = 0
while choice != 5:
    print("----------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("----------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice = int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        calc_cost()
    elif choice == 4:
        print_roll()
    else:
        print("Goodbye!")
