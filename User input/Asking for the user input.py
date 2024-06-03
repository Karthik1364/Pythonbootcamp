# asking for the user input in python.

# sometimes we would like to take the value for a variable from the user via their keyboard.
# for this purpose python provides a built-in function called input, so this function gets input from the user or from the keyboard.

# Ex:
print("what's your name?") # here it prints the string inside the print function, but here no way the user to be able to insert the data over here, which be used in our program.

# here istead of print function we use different function called "input function".
input("what is your name?")

# Ex:2
print("hello " + input("what is your name?")) # here is we have print function and inside the print function we have called input function in this case, which is nested function.

# whenever we run this code the input function part will be executed first,
# after giving the input then it will print hello with the given input inside the print function.

# Ex: 3
name = input("what is your name?\n") # here "\n" represents a new line break in the console.
print("hello " + name)

# note: "\n" which is special character that uses a line break.
# note: in python we use "\n" whenever we need new character.

# Ex:
print("hello\nword")

# we can use this inside string to get a new line character.
