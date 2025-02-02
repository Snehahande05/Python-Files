#Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {
    'dragon fruit': 5,
    'litchi': 2,
    'strawberry': 8,
    'pineapple': 1,
    'kiwi': 4
}
def sort_dict_ascending(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    return sorted_dict
def sort_dict_descending(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
sorted_asc = sort_dict_ascending(my_dict)
sorted_desc = sort_dict_descending(my_dict)
print("Original dictionary:", my_dict)
print("Sorted dictionary (ascending):", sorted_asc)
print("Sorted dictionary (descending):", sorted_desc)

#Write a Python program to remove duplicates from the dictionary. 
my_dict = {
    'apple': 5,
    'banana': 2,
    'orange': 5,
    'grape': 1,
    'kiwi': 4,
    'pear': 2
}
def remove_duplicates(d):
    
    unique_dict = {}
  
    seen_values = set()

    for key, value in d.items():
        if value not in seen_values:
         unique_dict[key] = value
        seen_values.add(value)

    return unique_dict
result_dict = remove_duplicates(my_dict)
print("Original dictionary:", my_dict)
print("Dictionary after removing duplicates:", result_dict)

#Write a Python program to combine two dictionary by adding values for common keys.
dict1 = {
    'sunflower': 8,
    'lily': 3,
    'rose': 5
}

dict2 = {
    'lily': 9,
    'rose': 1,
    'daisy': 6
}

def combine_dicts(d1, d2):
    combined_dict = d1.copy()  
    for key, value in d2.items():
        if key in combined_dict:
            combined_dict[key] += value
        else:
            combined_dict[key] = value
            return combined_dict

result_dict = combine_dicts(dict1, dict2)
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Combined dictionary:", result_dict)

#Write a Python program to create a dictionary from a string. ( Track the count of the letters from the string.)
input_string = "sneha hande"
def count_letters(s):
    letter_count = {}
    for char in s:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count
result_dict = count_letters(input_string)
print("Original string:", input_string)
print("Letter count dictionary:", result_dict)

#Write a Python program to match key and values both, in two dictionaries.
dict1 = {
    'red': 5,
    'yellow': 2,
    'orange': 8,
    'pink': 7
}

dict2 = {
    'yellow': 2,
    'pink': 7,
    'orange': 4,
    'red': 3
}
def find_matches(d1, d2):
    matching_pairs = {}
    for key, value in d1.items():
        if key in d2 and d2[key] == value:
            matching_pairs[key] = value

    return matching_pairs
matched_dict = find_matches(dict1, dict2)
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Matching key-value pairs:", matched_dict)


