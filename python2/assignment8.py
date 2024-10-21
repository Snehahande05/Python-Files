#Write a Python program to compute the element-wise sum of given tuples.Original :    (1, 2, 3, 4)   (3, 5, 2, 1)   (2, 2, 3, 1)
#Element-wise sum of the said tuples:  (6, 9, 8, 6)
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)
element_wise_sum = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))
print("Original tuples:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)
print("Element-wise sum of the tuples:", element_wise_sum)

#Write a Python program to convert a given list of tuples to a list of lists. 
#Original list of tuples: [(1, 2), (2, 3), (3, 4)]
original_list_of_tuples = [(1, 2), (2, 3), (3, 4)]
list_of_lists = [list(t) for t in original_list_of_tuples]
print("Original list of tuples:", original_list_of_tuples)
print("Converted list of lists:", list_of_lists)

#Convert the said list of tuples to a list of lists: [[1, 2], [2, 3], [3, 4]]
original_list_of_tuples = [(1, 2), (2, 3), (3, 4)]
list_of_lists = []
for t in original_list_of_tuples:
    list_of_lists.append(list(t))
print("Original list of tuples:", original_list_of_tuples)
print("Converted list of lists:", list_of_lists)

#Write a Python program to remove an empty tuple(s) from a list of tuples.
list_of_tuples = [(1, 2), (), (3, 4), (), (5, 6, 7), ()]
non_empty_tuples = [t for t in list_of_tuples if t]
print("Original list of tuples:", list_of_tuples)
print("List after removing empty tuples:", non_empty_tuples)

#Write a Python program to convert a given string to a tuple
original_string = "Sneha"
string_to_tuple = tuple(original_string)
print("Original string:", original_string)
print("Converted tuple:", string_to_tuple)

#Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
numbers = (8,5,2,9)
product = 1
for num in numbers:
    product *= num
print("Original tuple:", numbers)
print("Product of all the numbers:", product)