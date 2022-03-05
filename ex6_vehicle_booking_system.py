""" Vehicle Booking System
Allows staff to borrow a vehicle for the day and keep track of vehicles booked
Created by Joseph Wong
5/03/22
"""


# Booking Cycle Function
def booking_cycle():
    enter_seats = int(input("Number of seats needed in the vehicle "
                            "(-1 to quit) : "))
    while enter_seats != -1:
        print("All available vehicles to be booked: ")
        for vehicle in vehicle_pool:
            if vehicle[3] is True:
                if vehicle[2] >= enter_seats and vehicle[3]:
                    print(f"{vehicle[0]}  {vehicle[1]} - Seats: {vehicle[2]}")
                elif vehicle[2] < enter_seats and vehicle[3]:
                    print(f"{vehicle[0]}  {vehicle[1]} - Seats: {vehicle[2]}  "
                          f" - NOTE: Not enough seats")
        vehicle_num = int(input("Enter vehicle car number "
                                "you would like to book: "))
        enter_name = input("Enter your name for this vehicle: ")
        history = f"No. {vehicle_pool[vehicle_num-1][0]} - " \
                  f"{vehicle_pool[vehicle_num-1][1]} " \
                  f"- Booked by: {enter_name}"
        hired.append(history)
        print(f"{vehicle_pool[vehicle_num-1][1]} booked by {enter_name}")
        vehicle_pool[vehicle_num-1][3] = False
        print()
        enter_seats = int(input("Number of seats needed in the vehicle "
                                "(-1 to quit) : "))


# Main Routine
vehicle_pool = [[1, 'Suzuki Van', 2, True], [2, 'Toyota Corolla', 4, True],
                [3, 'Honda CRV', 4, True], [4, 'Suzuki Swift', 4, True],
                [5, 'Mitsubishi Airtrek', 4, True],
                [6, 'Nissan DC Ute', 4, True], [7, 'Toyota Previa', 7, True],
                [8, 'Toyota Hi Ace', 12, True], [9, 'Toyota Hi Ace', 12, True]]
hired = []
booking_cycle()
print("VEHICLES BOOKED TODAY")
for item in hired:
    print(item)
