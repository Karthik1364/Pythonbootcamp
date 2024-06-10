# Data Types - Weeks in Years
# Write a program that converts number of years to the weeks. if the input was 2, then the output should be 2 * 52 = 104, because we have 52 weeks in 1 year.

# Example Input:

# 2

# Example Output:

# 2 * 52 = 104

# There are 104 weeks in 2 years


# Hint:

# The prompt for input function has to be as shown below, otherwise the test case will not work.
'Enter number of years'

years = int(input('Enter number of years '))
weeks = years * 52
con1 = str(weeks)
con2 = str(years)
print('There are ' + con1, 'weeks in ' + con2, 'years')