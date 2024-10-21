# how to write a sentence on next line.
a=("This is my macos.\nI am writing python code in it.") 
print(a)
#how to give a space btw two sentences. 
b=("My favourite colour is black.\tI love to read books.")
print(b)

str1 = (" My name is sneha hande. \nI am 18 years old. \nMy hobbies are writing and reading. \nI love drawing also. \nI live in navi mumbai.")
print (str1)

#basic operations(concatenation)
str1 = ("hello")
str2 = ("kitty")
# print(str1 + str2)
# print(len(str1))
len1 = len(str1)
print (len1)
final_str = (str1 + str2)
print(str1 +" " +str2)
print(len(final_str))

#Indexing (it is basically assigning the value of the character for eg:- )
str = ("hello kitty")
char = str[5]
print(char)
ch = str[8] #t
print(ch)

#Slicing (dividing into parts)
#ending index is not included
str = ("sneha hande")
print(str[0:5])
print(str[ :11])
print(str[0: ])
print(str[-5:-1])
print(str[-11:-6])

str = ("this is my macos.")
str = (str.endswith("os."))
print(str)

str = ("this is my macos.")
str = str.capitalize()
print(str)

str = ("this is my macos.")
str = str.replace("my" , "sahil's")
print(str)

str = ("this is my macos.")
print(str.find("m"))
print(str.find("is"))
print(str.find("macos"))

a = ("my name is sneha. \n subway suffers is my favourite game. ")
print(a.count("is"))
print(a.count("subway"))
print(a.count("u"))

#write a program to input users first name and print its length.
a = str(input("Enter the name :"))
print(len(a))

#write a program to find the occurence of 's' in a string
str = ("sahils mom seema cooks very tasty foods at home.")
print(str.count("s"))

#conditional statements
#if-elif-else

age = 18
if (age >= 18 ):
    print("you are eligible for voting.")#identation i.e proper spacing is very imp in python
else:
    print("you are not eligible for voting.")

light = ("red")
if (light == "green"):
    print("go")
elif (light == "yellow"):
    print("wait")
elif (light == "red"):
    print("stop")            

#whenever if statement goes false then only elif statement works or it does not work .

num = 5
if (num > 2):
    print("the number is greater than 2")
if (num > 4):
    print("the number is greater than 4")    

num = 1
if (num > 2):
    print("the number is greater than 2")
elif (num > 4):
    print("the number is greater than 4")    
else:
    print("the number is less than 5")    

year = int(input("enter the year:"))
if (year %4 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.") 

marks = int(input("Enter students mark:"))
if (marks >= 90):
    print("grade A")
elif (marks >= 75 and marks<90):
    print("grade B")
elif (marks >=60 and marks<75):
    print("grade C")
else:
    print("grade D")

marks = int(input("Enter students mark:"))
if (marks >= 90):
    grade= "A"
elif (marks >= 75 and marks<90):
    grade ="B"
elif (marks >=60 and marks<75):
    grade ="C"
else:
    grade ="D"
print("Grade of the students :-" ,grade)   

# nesting
age = int(input("enter the age:-"))
if (age >= 18):
    if(age >= 80):
        print("cannot vote")
    else:
        print("vote")
else:
    print("cannot vote")            

# write a program to check if a number entered by the user is odd or even
number = int(input("Enter the number :-"))
if (number % 2 == 0):
    print("the number is even")
else:
    print("the number is odd")    
    
# write a program to find the greatest of 3 numbers entered by the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print("The greatest number is:", greatest)

# write a program to check if a number is a multiple of 7 or not
number = int(input("Enter a number: "))

if number % 7 == 0:
    print(f"{number} is a multiple of 7.")
else:
    print(f"{number} is not a multiple of 7.")

