# Create a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Add an element to the list
my_list.append(6)
print("List after adding 6:", my_list)

# Remove an element from the list
my_list.remove(2)
print("List after removing 2:", my_list)

# Modify an element in the list
my_list[0] = 10
print("List after modifying first element to 10:", my_list)

print("\n")

# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Add an element to the dictionary
my_dict['d'] = 4
print("Dictionary after adding {'d': 4}:", my_dict)

# Remove an element from the dictionary
del my_dict['b']
print("Dictionary after removing 'b':", my_dict)

# Modify an element in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying 'a' to 10:", my_dict)

print("\n")

# Create a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Add an element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Remove an element from the set
my_set.remove(2)
print("Set after removing 2:", my_set)


my_set.remove(1)
my_set.add(10)
print("Set after modifying 1 to 10:", my_set)