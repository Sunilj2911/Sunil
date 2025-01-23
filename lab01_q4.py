# Create a list of numbers from 1 to 10000
list = [i for i in range(1, 10001)]

# Create lists based on the remainder when divided by 5
list0 = [i for i in range(1, 10001) if i % 5 == 0]
list1 = [i for i in range(1, 10001) if i % 5 == 1]
list2 = [i for i in range(1, 10001) if i % 5 == 2]
list3 = [i for i in range(1, 10001) if i % 5 == 3]
list4 = [i for i in range(1, 10001) if i % 5 == 4]

# Print the lists
print(list0)
print(list1)
print(list2)
print(list3)
print(list4)

# Combine all lists into a new list
new_list = []
new_list.extend(list0)
new_list.extend(list1)
new_list.extend(list2)
new_list.extend(list3)
new_list.extend(list4)

# Check if all numbers from 1 to 10000 are present in new_list
if set(new_list) == set(list):
    print("True")
else:
    print("False")
