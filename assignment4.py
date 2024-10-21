#1) python program to check whether the string is symmetrical or palindrome(kasak)
string=str(input("enter the name:-"))
if string == string[::-1]:
    print("The string is palindrome.")
else:
    print("The string is not a palindrome.")

#2) find length of a string in python without len function    
string=input("enter the string:-")
count=0
for char in string:
     count+= 1
print(f"the length of the string is : {count}")   

#3) python program to remove all duplicates from a given string
string = input("Enter a string: ")
result = ""
for char in string:
   if char not in result:
      result += char
print(f"The string after removing duplicates: {result}")    

#4) Maximum frequency character in String
string = input("Enter a string: ")
frequency ={}
for char in string:
    if char in frequency:
        frequency[char] += 1  
    else:
        frequency[char] = 1  
max_char = ''
max_freq = 0
for char in frequency:
    if frequency[char] > max_freq:
        max_freq = frequency[char]
        max_char = char
print(f"The character with the maximum frequency is: '{max_char}'")
print(f"It appears {max_freq} times.")                

#5) write a python program to count the numbers of characters in a string.
Sample string:"google.com"
Expected Result : {'g':2,'o':3,'l':1,'e':1,'.':1,'c':1,'m':1}
string = input("Enter a string: ")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)    
 
# 6) Count all letters, digits, and special symbols from a given string
string = input("Enter a string: ")
letters_count = 0
digits_count = 0
special_count = 0
for char in string:
    if char.isalpha():  # Check if the character is a letter
        letters_count += 1  # Increment letter count
    elif char.isdigit():  # Check if the character is a digit
        digits_count += 1  # Increment digit count
    else:  # If it's neither a letter nor a digit, it is a special symbol
        special_count += 1  # Increment special symbol count
print(f"Letters: {letters_count}")
print(f"Digits: {digits_count}")
print(f"Special Symbols: {special_count}")

#7) Write a program which read incoming email, all emails not sent from the "@itm.edu" domain
#should be moved to the spam box.
incoming_emails = [
    {"sender": "disha.rao@itm.edu", "subject": "Meeting Reminder"},
    {"sender": "sneha.hande@gmail.com", "subject": "Hello!"},
    {"sender": "nivedita@itm.edu", "subject": "Project Update"},
    {"sender": "prity@yahoo.com", "subject": "Spam Offer"},
]
inbox = []
spam_box = []
for email in incoming_emails:
    # Check if the sender is from the "@itm.edu" domain
    if email["sender"].endswith("@itm.edu"):
        # If it's from the allowed domain, add it to the inbox
        inbox.append(email)
    else:
        # Otherwise, move it to the spam box
        spam_box.append(email)
print("Inbox:")
for email in inbox:
    print(f"Sender: {email['sender']}, Subject: {email['subject']}")
print("\nSpam Box:")
for email in spam_box:
    print(f"Sender: {email['sender']}, Subject: {email['subject']}")

#a8)  You are tasked to create a simple password validator. The validation rules are as follows:
# Password length of at least 8 characters.
# At least one uppercase character.
# At least one lowercase character.
# At least one "special" character from the following set of characters: "!#$%&*+-.?~"

#Function to validate the password
def is_valid_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Initialize flags for validation checks
    has_upper = False
    has_lower = False
    has_special = False
    special_characters = "!#$%&*+-.?~"

    # Loop through each character in the password
    for char in password:
        if char.isupper():  # Check for uppercase character
            has_upper = True
        elif char.islower():  # Check for lowercase character
            has_lower = True
        elif char in special_characters:  # Check for special character
            has_special = True

    # Return True only if all conditions are met
    return has_upper and has_lower and has_special

# Get input from the user
password = input("Enter a password to validate: ")

# Validate the password
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Make sure it meets the following criteria:")
    print("- At least 8 characters long")
    print("- At least one uppercase character")
    print("- At least one lowercase character")
    print("- At least one special character from: !#$%&*+-.?~")


