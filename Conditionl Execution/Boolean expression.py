# Boolean expression

# The python boolean type has only two possible values
# 1. True
# 2. False

# Boolean expressions are very crucial when it comes to conditional execution.

# If you want to check an expression, whether it's true or false, we are using operators.
# Now the first operator is "equal operator" which is "equal sign" (==) from math.

#### "==" equal:
# so if you want to check that if two vaules are equal, we need to use equal sign over here.
# here you need to take into account that equal sign is different from the equal sign that we use in maths, i.e "=" this single sign we use it in the maths.
# But here in python, the equal sign is denoted by double equal "==" sign over here.
# for example. if I want to check an expression like this.

# Ex: 1:
print(1 == 1) # in this case it returns True.

# note: single equal "=" sign in python is used as assignment operator.
# note: if you use "==" sign over here, it's becoming an expression.

# Ex: 2:
print(1 == 2) # in this case it returns False.

# Ex: 3:
print(type(True)) # here the True belongs to "bool" type.
print(type(False)) # here the False belongs to "bool" type.

# note: this means that these values over here is not string, they are just type of "bool" class.
# note: in python when we are writing boolean values, we need to start first letter in capital letter, then rest of the letters should be lower letters.

#### "!=" not equal:
# so in this case, if you want to check two values, if they are not equal to each other, we are using exclamation mark with equal sign.

# Ex: 1:
print(1 != 2) # here it returns True becasue 1 is not equal to 2.
print(1 != 1) # here it returns False because 1 is equal to 1.

#### ">" greater than sign:
print(2 > 1) # it prints True.

#### "<" less than sign:
print(2 < 1) # it returns False.

#### ">=" greater than or equal to:
print(2 >= 1) # it returns True.

# note: the greater than or equal to won't works "=>" this way.

#### "<=" less than or equal:
print(2 <= 1) # it returns False.

#### is not:
# "Is not" operator means that X is not same as Y.
# in this case, when we are using "is not" operator, first we need to create "variables".

# Ex: 1
x = 1
y = 2
print(x is not y) # here it returns True.

# Ex: 2
x = 2
y = 2
print(x is not y) # here it returns False.

# note: if we write straight away "1 is not 2" in this case we get error, so we can only use variable for the to define "is not" operator.
