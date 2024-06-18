# Multiple if Statement:

# In the chain condition we saw how we colud use if/elif statements for multiple conditions.
# But here you need to be very careful that even though we have multiple conditions, we are only checking on condition.

# id condition1:   # here is condition 1, if the condition 1 is not met, we so with condition 2.
#   do A
# elif condition2: # here in condition 2, if this is met, we are going to do B.
#   do B
# else:            # otherwise we are going to do else statement over here.
#   do this

# because, if this first condition is ture, then we are going to do A and we are going to bypass everything.
# if this not true, we are going to continue to the second condition and we are going to chech that if the second condition is true, we are going to do B and we are going to bypass else over here.

#### note: what if you were in a situation where you need to check for multiple conditions, even the previous one was already true.
# so we might have a condition that if this first condition is true, we want to check the second condition as well.


#### Excercise:

# so let's say you have got a job at a mortgage bureau and first job of the day is that to write some code that identifies if someone is eligible for a mortgage or not.
# firstly, inorder for somebody to actually get a mortgage, their salary has to be above $2000.
# so if somebody's credit score is greater than 800, the interest rate will be 4%.
# so if somebody's credit score is less and equal to 800, the inerest rate in this case will be 6%.
# disabled person will get -2% discount from the interest rate.

print("Welcome to the mortgage calculator")
salary = int(input("Enter your salary: $"))
rate = 0
if salary > 2000:
    print("You are eligible for the mortgage")
    credit_score = int(input("Enter you credit score: "))
    if credit_score > 800:
        rate = 4
        print("your interest is 4%")
    elif credit_score > 750:
        rate = 6
        print("your interest rate is 6%")
    else:
        rate = 8
        print("your interest is 8%")
    disability = input("Are a disabled person: ")
    if disability == "y":
        rate -= 2 # We are decreasing rate by two over here.
    print(f"final interest rate: {rate}%")
else:
    print("Sorry! you are not eligible for the mortgage")

# Code line 45: In python as well as in many other languages, there is actually slightly shorter way of writing this.
############### So when you want to decrease the current value that is held in a variable and you want to save it back to the same variable here, you can simply use minus and equal sign over here (-=).  
