# strings and rounding numbers.

# so instead of doing all these conversions and concatenations over here, we can use "F sting".
# "F string" allows us to combine all different data types together without converting and concatenating.
# note: in front of string we just need to type "F".

year = input('Enter number of years ')
weeks = 52 * int(year)
# print('There are ' + str(weeks), 'weeks in ' + year, 'years')

# F string:
print(f'There are {weeks} weeks in {year} years')

# note: here the f should be placed before the double or single quotes.
# note: and we are putting the variables (that needs to be converted) inside curly braces "{}" over here.

# by using "f string" you cut down a lot of manual work of inserting different data types of data into string.
