# the operators are symbols that represent competitions like addition, multiplication or some other mathematical operations.

# + Addition
# - Substraction
# * Multiplication
# / Division

print(1 + 1)
print(3 - 2)
print(2 * 3)
print(4 / 2) # whenever we divide a number the result will always be in the floating point number (2.0).
print(4 // 2) # use "//" if we want to ignore the floating number as the result (2).
print(5 ** 2) # by writing two asterisks "**" we can raise the number to the power of given second number.

# PEMDAS rule:

# P = Parentheses
# E = Exponents
# M = Multiplication
# D = Division
# A = Addition
# S = Subtraction

## so by using this pemdas rule, we can identify the priority of the opertions in python as we have in mathematics.
## note: here multiplication and division are equally important, PEMD||AS, here PEMD is the priority and AS is secondary.

# Ex: 1
print(2*2+2/2-2)

# Ex: 2
print(11 // 3) # "//" operator is used to get the quotient.
print(11 % 3) # (modulus %) operator is used to get the remainder.

# note: there might be situation that you want to check whether one number is divisible by another
# so if the result from modulus operator is zero, it means that the first number is divisible by second number.

# Ex: 3
print(12 % 3) # it will return zero.

# note: so by calling the modulus operator, we can identify if any number is divisible by the second number or not.

# Ex: 4
print(12 % 10) # if I put 10 instead of 3, you will see that it is going to extract the second number form this two digit number.

# if you want to extract the one digits you can put 10.
# if you want to extract both digits you can put 100.

# Ex: 4
print(12 % 100)