# IF & ELSE:

# if one condition is True, we are doing one thing.
# if one condition is not True, we are doing another thing.

# example for the IF & ESLE:

# if condition: if this condition is True.
#   do this     we are going to execute this part of code over here.
# else:         here if the condition is not true, then we will skip the above.
#   do this     and execute this code.

# note: in python indentation is very important.

# Ex: 1:

temperature = 15
if temperature > 20:
    print("do not wear a coat!")
else:
    print("wear a coat!")

# Ex: 2:

# so let's say you have got a job at a mortgage bureau and first job of the day is that to write some code that identifies if someone is eligible for a mortgage or not.
# firstly, inorder for somebody to actually get a mortgage, their salary has to be above $2000.

# using ">" greater than:
print("Welcome to Mortgage Calculator!")
salary = int(input("Enter your salary: $"))
if salary > 2000:
    print("you are eligible for mortgage!")
else:
    print("sorry, you are not eligible")

# using ">=" greater than or equal to:
print("Welcome to Mortgage Calculator!")
salary = int(input("Enter your salary: $"))
if salary >= 2000:
    print("you are eligible for mortgage!")
else:
    print("sorry, you are not eligible")

# using "!=" not equal:
print("Welcome to Mortgage Calculator!")
salary = int(input("Enter your salary: $"))
if salary != 2000:
    print("you are eligible for mortgage!")
else:
    print("sorry, you are not eligible")
# here "!=" means exactly equal to $2000 are not eligible for the mortgage, except $2000 everything is eligible for the mortgage.

# note: we can also execute "if condition" without "else" part.
# note: everytime we don't need to put "else" part, we can also skip this "else" part.

# using "pass" keyword:

print("Welcome to Mortgage Calculator!")
salary = int(input("Enter your salary: $"))
if salary > 2000:
    pass # when writing a code and you don't know what you are going to put over here, for example if the conditio is met, you don't remember that what you are going to put over here, so you can put just "pass" keyword over here.
else:
    print("sorry, you are not eligible")

# pass keyword does nothing, it will skip the part of the code here.