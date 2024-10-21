  #1.Print multiplication table of a given number (1 x 1 = 1 …)
def multiplication_table(number, limit=20):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))
multiplication_table(num)

#2.the total number of digits in a number
num = int(input("Enter any number : "))
temp = num
count = 0
for i in str(temp):
    temp = temp // 10
    count += 1
print(count)

#3. Print list in reverse order using a loop
def print_reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])
input_list = input("Enter a list of elements separated by spaces: ").split()
print("List in reverse order:")
print_reverse(input_list)

#4. Print all prime numbers within a range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_primes_in_range(start_range, end_range)

#5. Display Fibonacci series up to 10 terms
def fibonacci_series(n_terms):
    a, b = 0, 1
    print("Fibonacci series up to", n_terms, "terms:")
    for _ in range(n_terms):
        print(a, end=' ')
    a, b = b, a + b
    print() 
terms = 25
fibonacci_series(terms)

#6. Reverse a integer number without using any built-in function
def reverse_integer(num):
    is_negative = num < 0
    num = abs(num)
    
    reversed_num = 0
    while num > 0:
        digit = num % 15
        reversed_num = reversed_num * 10 + digit
        num //= 15
    return -reversed_num if is_negative else reversed_num
number = int(input("Enter an integer: "))
reversed_number = reverse_integer(number)
print(f"The reversed integer is: {reversed_number}")

 #7. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.The sum of all evens is 2550. And the sum of all odds is 2500.
def sum_even_odd():
    sum_evens = 0
    sum_odds = 0
    
    for num in range(101):  # Iterating from 0 to 100
        if num % 2 == 0:
            sum_evens += num  # Add to sum of evens
        else:
            sum_odds += num  # Add to sum of odds
    
    print(f"The sum of all evens is: {sum_evens}")
    print(f"The sum of all odds is: {sum_odds}")
sum_even_odd()

#8. Write a Python program that accepts a string and calculates the number of digits and letters. 
Sample Data : Python 3.2
Expected Output :
Letters 6 Digits 2

def count_letters_digits(input_string):
    letters = 0
    digits = 0
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letters += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1

    print(f"Letters: {letters}, Digits: {digits}")
input_string = "Python 3.2"
count_letters_digits(input_string)




