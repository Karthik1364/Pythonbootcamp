# Gross pay project:

# Instruction:
# Write a program to prompt the user for hours and rate per hour to compute gross pay. You need to take into account that the result has exactly two digits after the decimal place.

# Input:
# Enter Hours: 35
# Enter Rate: 2.75

# Output:
# Pay: 96.25

# Solution:
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
hours = float(hours)
rate = float(rate)
pay = round(hours*rate,2)
print(f"Pay: {pay}")

# OR

hours = input("Enter Hours: ")
rate = input("Enter Rates: ")
pay = float(hours) * float(rate)
pay = round(pay,2)
print(f"Pay: {pay}")