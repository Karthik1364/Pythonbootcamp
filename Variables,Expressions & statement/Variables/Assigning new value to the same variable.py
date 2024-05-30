# variable is a container that stores the information.
# note: the variable by its name, the values can be changed or varied, that's why it is called variable.
# if the new variable is created with the same name.

# use case: 1
name = "karthik"
print(name) # it print the name karthik

# later i have decided to give this same varible with the different name or data.

name = "saravanan"
print(name) # it prints the name saravanan

# now both name is printed here.
# first the name variable is holding the value karthik and again it is holding value saravanan.

# because before printing out this variable, i have assigned new value to it.

# use case: 2
name = "karthik"
name = "saravanan" # i have given the new value to this variable,
print(name) # it print the value saravanan.

# after this assignment, whenever you refer to name, it's going to print saravanan instead of karthik.
# note: this means that the variable keeps the last value that we assigned to it.
# note: we cannot start the variable name with the numbers, because it give syntax error.
# note: we can start the varible with the uppercase and it's better to start the variable with the lowercase.
# note: we can use underscore to our variable.
my_name = "karthik"
print(my_name)

# some people use camel case.
myName = "karthik"
print(myName)

# keep in mind that if we give a variable an illegal name, you will get syntax error.
# note: illegal names like -> we cannot start the variable name with the numbers,
# note: we cannot use characters like @ characters, before or after the variable name.
# note: we cannot use the python keywords like if, ifelse, and, as, del, from, None, True, False, def, import etc...
# we have 35 keywords in python that cannot be used as the variable name, those are called reserved names in python.

class = "karthik"
print(class) # it gives the syntax error.