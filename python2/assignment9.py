#Write a Python program to remove an item from a set if it is present in the set.
my_set = {7,4,9,2,6}
item_to_remove = 2
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Item {item_to_remove} removed from the set.")
else:
    print(f"Item {item_to_remove} is not present in the set.")
print("Updated set:", my_set)

#Write a Python program to check if two given sets have no elements in common.
set1 = {11,12,13,14}
set2 = {15,16,17,18}
if set1.isdisjoint(set2):
    print("The two sets have no elements in common.")
else:
    print("The two sets have some elements in common.")
print("Set 1:", set1)
print("Set 2:", set2)

#Write a Python program toGet Only unique items from two sets
set1 = {8,6,4,2}
set2 = {3,5,6,8}
unique_items = set1.symmetric_difference(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Unique items from both sets:", unique_items)

#Write a Python program to Convert Set to one String
my_set = {'s', 'n', 'e', 'h', 'a'}
set_to_string = ''.join(my_set)
print("Original set:", my_set)
print("Converted string:", set_to_string)

#program to count number of vowels using sets in given string
input_string = "Hii,myself Sneha manoj hande.I am studying B-TECH CSE."
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
print("Input string:", input_string)
print("Number of vowels:", vowel_count)