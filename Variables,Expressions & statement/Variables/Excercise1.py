# Switch values - python program.
# write a program that switches the values stored in the variales "a" and "b".
# a = 10
# b = 20

# output:
# a = 
# 20
# b = 
# 10

# solution:

a = 10
b = 20

c = a  # c = 10   if "c = a" then "a" will become empty.
a = b  # 10 = 20  then "a = b" the empty a will be filled with "b", now "b" is empty.
b = c  # 20 = 10  now the empty "b" will become "c",

print("a =")
print(a)
print("b =")
print(b)