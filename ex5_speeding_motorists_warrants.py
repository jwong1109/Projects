""" Speeding motorists and warrants
Keep track of speeding tickets and alerts for outstanding warrants
Created by Joseph Wong
3/03/22
"""


# Name of Speeder Function
def name_speeder():
    enter_name = input("Enter name of speeder: ('X' to stop input) ").title()
    if enter_name in wanted:
        print(f"{enter_name.upper()} - WARRANT TO ARREST")
    name_list.append(enter_name)
    return enter_name


# Amount Speeding Function
def over_limit():
    amount_speed_limit = int(input("Enter the amount over speed limit: "))
    amount_over_list.append(amount_speed_limit)
    return amount_speed_limit


# Calculate Fine Function
def calculate_fine():
    limit = over_limit()
    if limit < 10:
        calculating_fine = 30
    elif limit <= 14:
        calculating_fine = 80
    elif limit <= 19:
        calculating_fine = 120
    elif limit <= 24:
        calculating_fine = 170
    elif limit <= 29:
        calculating_fine = 230
    elif limit <= 34:
        calculating_fine = 300
    elif limit <= 39:
        calculating_fine = 400
    elif limit <= 44:
        calculating_fine = 510
    else:
        calculating_fine = 630
    return calculating_fine


# Main Routine
wanted = ['James Wilson', 'Helga Norman', 'Zachary Conroy']
name_list = []
amount_over_list = []
total_fines = 0
total_amount_fines = 0
print("##########")
name = name_speeder()
while name != "X":
    fine = calculate_fine()
    print(f"{name} to be fined ${fine}")
    total_fines += 1
    total_amount_fines += fine
    print("##########")
    name = name_speeder()
print(f"Total fines: {total_fines}")
final_list = []
for amount in amount_over_list:
    each_section = (amount_over_list.index(amount))
    each_person = (name_list[each_section])
    final_list.append(f"{each_section + 1}) Name: {each_person}    "
                      f"Amount over Limit: {amount}")
for roll in final_list:
    print(roll)
print(f"Total amount of fines: ${total_amount_fines}")
