 #Write a Python function to check whether a number falls within a given range.
def is_in_range(number, lower_bound, upper_bound):
    if lower_bound <= number <= upper_bound:
        return True
    else:
        return False
print(is_in_range(5, 1, 10))  
print(is_in_range(15, 1, 10)) 

#   Write a Python function that takes a list of strings as input and returns a tuple containing the shortest and longest word from the list
def find_shortest_and_longest(words_list):
     if not words_list:
        return None, None 
     shortest_word = min(words_list, key=len)
     longest_word = max(words_list, key=len)
     return shortest_word, longest_word
words = ["apple", "banana", "cherry", "date", "elderberry"]

result = find_shortest_and_longest(words)
print(result)  # Output: ('date', 'elderberry')

# Write a Python function that takes a list and an element as input. The function should add the element to the list only if it's not already present in the list.
def add_element_if_not_present(my_list, element):
    if element not in my_list:
        my_list.append(element)
    return my_list
my_list = [1, 2, 3, 4]
updated_list = add_element_if_not_present(my_list, 5)
print(updated_list)  
updated_list = add_element_if_not_present(my_list, 3)
print(updated_list)

#Write a program to implement these formulae of permutations and combinations. 
#Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
#Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        return result
def permutations(n, r):
    return factorial(n) // factorial(n - r)
def combinations(n, r):
    return permutations(n, r) // factorial(r)
n = 5 
r = 3  
print("Permutations p(5, 3):", permutations(n, r))  
print("Combinations c(5, 3):", combinations(n, r)) 

# A number is called perfect if the sum of proper divisors of that number is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range
def find_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    
    return divisors
def is_perfect_number(num):
    divisors_sum = sum(find_divisors(num))
    return divisors_sum == num
def print_perfect_numbers_in_range(start, end):
    print(f"Perfect numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_perfect_number(num):
            print(num)
start = 1
end = 10000 
print_perfect_numbers_in_range(start, end)

# Write a recursive function that will return the nth term of the Fibonacci sequence.
#The sequence has a relationship of Fn = Fn-1 + Fn-2 with F0 = 0 and F1 = 1, where n=0,1,2,3,4,5,...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    
n = 6 
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci sequence is: {result}")        