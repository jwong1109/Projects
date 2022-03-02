""" Taxi Trips v1 - to keep track of details for a taxi
Created by Joseph Wong
28/02/2022
"""


BASE_COST = 10
EXTRA_COST = 2
total_time = 0
total_trip = 0
total_income = 0
name = input("What's the driver's name? ").title()
trip = input("Do you want to start a new trip? ").title()
while trip != "No":
    time = int(input("How long in minutes did the trip take? "))
    total_trip += 1
    total_time += time
    cost = BASE_COST + EXTRA_COST * time
    total_income += cost
    print(f"The cost for the trip is ${cost}")
    trip = input("Do you want to start a new trip? ").title()
ave_time = total_time / total_trip
ave_cost = total_income / total_trip
print(f"Driver's name: {name}")
print(f"The total time of all trips: {total_time} minutes.")
print(f"The average time of all trips: {ave_time:,.2f} minutes.")
print(f"The total income for the day: ${total_income}")
print(f"The average cost of all trips: ${ave_cost:,.2f}")
