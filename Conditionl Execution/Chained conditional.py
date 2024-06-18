# Chained Conditional:

# What is chained conditionals?
#### sometimes there are more than two possibilities, and we need more than two branches over here.
# so in this case, we are going to express a competition like this with a chained conditional.
# so here, we use chain conditional with ELIF statement, which is an abbrevation of "else if" condition.

# note: instead of having simple if/else statement where there is only one condition.

# if condition: # if this condition is true we need to do this.
#   do this
# else:         # otherwise we need to do this.
#   do this

# here we are going to have more than one condition, so you can add as many ELIF condition as you want.

#### using chain condition our condition will be like this. (if/elif/else)

# id condition1:   # here is condition 1, if the condition 1 is not met, we so with condition 2.
#   do A
# elif condition2: # here in condition 2, if this is met, we are going to do B.
#   do B
# else:            # otherwise we are going to do else statement over here.
#   do this

# note: we can add as many as ELIF condition as we want.
# note: but here you need to take into account that if you have else statment, you have to put this else statement outside the ELIF statement of at the end of the else statement.
# note: you can also skip else statment or you can add else statement at the end.
# note: else statement means that if none of these conditions were true, we can do this else statement.
 
#### nested if condition:
# x = 1
# y = 1
# if x == y: # here if the x and y are equal, it prints that x and y are equal.
#     print("x and y are equal")
# else:  # here if the x and y are not equal, the else part will be executed.
#     if x > y:
#         print("x greater than y")
#     else:
#         print("x less than y")

# #### chain condition:
# if x > y:
#     print("x greater than y")
# elif x < y:
#     print("x less than y")
# else:
#     print("x and y are equal")

# note: no matter how many ELIF statements you are going to write in this case, only one of them will be executed.
# note: and each condition will be checked in order.
# note: if one condition is false, the next one will be checked, and if the next one is false, and it will continue to the next one.
# note: if one of them is true, the corresponding branch will executes and the statments ends over here.
# note: if more than one condition is true, only the first branch will be executed.

# Excercise:

# so let's say you have got a job at a mortgage bureau and first job of the day is that to write some code that identifies if someone is eligible for a mortgage or not.
# firstly, inorder for somebody to actually get a mortgage, their salary has to be above $2000.
# so if somebody's credit score is greater than 800, the interest rate will be 4%.
# so if somebody's credit score is less and equal to 800, the inerest rate in this case will be 6%.
print("Welcome to the mortgage calculator")
salary = int(input("Enter your salary: $"))
if salary > 2000:
    print("You are eligible for the mortgage!")
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 800:
        print("Your interest rate is 4%")
    elif credit_score > 750:
        print("Your interest rate is 6%")
    else:
        print("your interest rate is 8%")
else:
    print("Sorry! you are not eligible for the mortgage!")
    
    