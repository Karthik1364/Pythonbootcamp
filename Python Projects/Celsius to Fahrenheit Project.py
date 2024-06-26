# Celsius to Fahrenheit project:

# Instruction:
# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature. Formula : (°C × 9/5) + 32 = °F

# Input:
# Enter Temperature in Celsius: 10

# Output:
# 10 Celsius = 50 Fahrenheit

# Solution:
celsius = int(input("Enter Temperature in Celsius: "))
fahrenheit = round((celsius * 9 / 5) + 32)
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

# OR

celsius = input("Enter Temperature in Celsius: ")
fahrenheit = round((int(celsius)*9/5) + 32)
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")