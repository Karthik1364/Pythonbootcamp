# Nested Condition:

# means one condition can be also nested within another condition.

# example for the IF & ESLE:

# if condition: # if this first condition is True,
#   if another condition: # we are continuing to another if condition over here.
#       do this     # if this condition is ok will execute this.
#   else:
#       do this  # if not this condition will be executed inside the if condition.
# else:         
#   do this   # if the above "if inside if condition" is not correct, we will process with the outside else part.

# note: once the first condition has passed, we can check for another condition and then we can have another if/esle statement inside this if condition over here.

### Example: 1
# in this condition we are checking if x is equal to y or not.
# if it is equal to y, we are printing out x and y are equal.
# if they are not equal, we are printing out they are not equal.
x = 1
y = 3
if x == y:
    print("x and y are equal")
else:
    print("x and y are not equal")

# let's say if we have another condition, which we need to check that if x is greater than y or not. so in this case we need nested if condition.
# so we are going to write nested if condition inside else statement over here.
# so if they are not equal, we are going to check another of condition if x greater than y or not.
if x == y: # here if the x and y are equal, it prints that x and y are equal.
    print("x and y are equal")
else:  # here if the x and y are not equal, the else part will be executed.
    if x > y:
        print("x greater than y")
    else:
        print("x less than y")