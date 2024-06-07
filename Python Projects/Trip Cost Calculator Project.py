# Trip Cost Calculator Project:

# Instruction:
# Write a program which calculates trip cost for a user.

# 1: Create a greeting for your program.
# 2: Ask the user for number of days.
# 3: Ask the user for hotel price.
# 4: Ask the user for flight price.
# 5: Ask the user for rental car price.
# 6: Ask for other expenses.
# 7: Combine all expenses together and print with 2 digits after decimal places.

# Input:
# Welcome to the Trip Cost Calculator!
# How many days will you stay? 3
# How much does hotel cost per night? $30
# How much does flight cost? $50
# If you need rental car please enter the price otherwise enter zero. $10
# Enter other possible expenses $0

# Output:
# Total Cost: $170.0

# Solution:
print("Welcome to the Trip Cost Calculator!")
number_of_days = int(input("How many days will you stay? "))
hotel_price = float(input("How much does hotel costper night? $"))
flight_price = float(input("How much does flight cost? $"))
rental_car_price = float(input("If you need rental car please enter the price otherwise enter zero $"))
other_expenses = float(input("Enter other expenses $"))
total_cost = number_of_days * hotel_price + flight_price + rental_car_price * number_of_days + other_expenses
print(f"Total Cost: ${total_cost}")
