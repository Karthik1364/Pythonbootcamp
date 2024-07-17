# list = [1,0,2,0,4,6]

# for item in list:

#     if item == 0:

#         list.remove(list)
#         list.append(list)

# print(list)


lst = [1, 0, 2, 0, 4, 6]

# Count the number of zeros
zero_count = lst.count(0)

# Remove all zeros from the list
lst = [item for item in lst if item != 0]

# Append the zeros to the end of the list
lst.extend([0] * zero_count)

print(lst)
