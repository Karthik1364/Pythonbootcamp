# How do length function works?

# Ex: 1
# basically length function starts with keyword "len".
# Ex: len()

print(len("karthik"))

# Ex: 2
# here we have parenthesis, then inside the parenthesis we need to provide "string", to count the number of characters.

print(len("hello world"))

# Ex: 3
# note: len() function does not like working with integers, and by forcing the rule, we end up with an error and our code breaks and gives us type error.

print(len(10)) # it gives type error, so length function doesn't accept integer.

# Ex: 4
# If I want to print proper message to the console, like "your name has six characters"
# In this case I need to use concatenation inside print function so we will write something like this,

name = input("What is your name? ")
length = len(name)
print("your name has" + length + "characters") # here it gives error because we cannot concate str with int.

# Ex: 5
# to find the type of the length.
name = input("What is your name? ")
length = len(name)
print(type(length)) # with this we can find the type of the len function.

# Ex: 6
# here to convert the int to str, we need to convert the datatype to str.
name = input("What is your name? ")
length = len(name)
print(type(length))
newLength = str(length) # here the int is converted to str.
print(type(newLength))

# Ex: 7 
# now here we can do the concatenation.
name = input("What is your name? ")
length = len(name)
newLength = str(length)
print("Your name has " + newLength + " characters")

# note: not only str, we can also convert the bunch of datatype to the concerned datatype.

# float:
a = 123
a = float(a) # here i have converted int to float.
print(type(a))

# int:
a = 123.13
a = int(a) # here i have converted float to int.
print(type(a))

# note: finally we can easily convert many datatype to other datatype using function over here.
# note: we can use functions like "str(), int(), float()" to convert that datatype to another data type.