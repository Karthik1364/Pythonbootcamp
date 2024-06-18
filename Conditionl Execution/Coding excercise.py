# Body Mass Index (BMI) calculator:

# Write a program that calculates  the Body Mass Index (BMI) based on a user's weight and height and interprets it based BMI graph below.


# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 their weight is normal
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese

#### solution:
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2,2) # it is going to be the square.
if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, your weight is normal.")
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
else:
    print(f"your bmi is {bmi}, you are obese.")