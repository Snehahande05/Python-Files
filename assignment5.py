#Write a Python program to reverse the order of the items in the array.
my_array = [9,8,7,6,5]
my_array.reverse()
print("Reversed Array:", my_array)

#Write a Python program to get the number of occurrences of a specified element in an array.
my_array = [4,7,5,9,2,5,8,2,5,1,3,5,6,0,5]
element_to_count = 5
count = my_array.count(element_to_count)
print(f"The element {element_to_count} occurs {count} times in the array.")

# Write a Python program to find out if a given array of integers contains any duplicate elements.
my_array = [6,8,4,6,0,3,2]
unique_elements = set(my_array)
if len(my_array) != len(unique_elements):
    print("The array contains duplicates.")
else:
    print("The array does not contain any duplicates.")

#  Write a  Python program to find the missing number in a given array of 5 continuous numbers.
my_array = [11,13,14,15]  # Missing number is 12
n = 5  # Total numbers (continuous)
expected_sum = sum(range(11, n + 11))
actual_sum = sum(my_array)
missing_number = expected_sum - actual_sum
print(f"The missing number is: {missing_number}")

#Replace all odd numbers in the given array with -1
my_array = [5, 6, 7, 8, 9]
for i in range(len(my_array)):
    if my_array[i] % 2 != 0:  # Check if the number is odd
        my_array[i] = -1  # Replace odd number with -1
print("Modified Array:", my_array)