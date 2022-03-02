""" Absences at work - to record data about absences in a work
Created by Joseph Wong
1/03/22
"""


# Recording Absences Function
def record_absences():
    name = input("Enter name: ")
    while name != "$":
        employee_roll.append(name)
        total_days = int(input("Days absent from work in the last year: "))
        if total_days == 0:
            no_absence.append(name)
        absence_days.append(total_days)
        name = input("Enter name: ")


# Main Routine
employee_roll = []
absence_days = []
no_absence = []
record_absences()
average_absent = sum(absence_days) / len(absence_days)
print(f"Average number of days staff were absent: {average_absent:,.2f}")
most_days = max(absence_days)
section_most = (absence_days.index(most_days))
person_most = employee_roll[section_most]
print(f"Person with most days absent: {person_most} with {most_days} days")

# List of people with zero-absences
print(f"List of people not absent at all: ")
no_absence.sort()
for people in no_absence:
    print(people)

# List of people above average
above_average = []
for days in absence_days:
    if days > average_absent:
        days_above_average = days
        section_above_average = (absence_days.index(days_above_average))
        person_above_average = (employee_roll[section_above_average])
        above_average.append(f"{person_above_average}, {days_above_average}")
print(f"List of people absent above average: ")
above_average.sort()
for people in above_average:
    print(people)
