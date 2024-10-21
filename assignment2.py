
#1.  write a program to check whether an years is leap year or not 
year = int(input("enter the year:"))
if (year %4 == 0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")    

#2. write a program to check whether a number entered is three digit number or not 
a=int(input("enter the number"))
if a>99:
            print("yes number is three digit number")
else:
            print("number is less than 100")

#3. write a program to check whether a person is eligible for voting or not (voting age>=18)
age=int(input("enter the age"))            
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible")

#4. write a program to check whether the last digit of a number(entered by user) is by 3 .
number= int(input("enter the number"))
if number %10==3:
       print("last digit is 3")
else:
       print("last digit is not 3")

#5. write a python program to check whether an alphabet is a vowel or consonant.
alphabet = str(input("enter the alphabet"))
if (alphabet =='a' or alphabet == 'e' or alphabet =='i' or alphabet =='o' or alphabet=='u'):
      print("vowel")
else:
      print("consonant")  

#6. write a python program to convert a month name to a number of days.
x= str(input("enter month name"))
if x == "january" or x== "march" or x== "may" or x== "july" or x== "august" or x== "october" or x== "december":
    print("It has 31 days")
elif x=="february":
    print("It has 28 or 29 days")
else:
    print("It has 30 days")
  
#7. write a program to check if a triangle is equilateral,isoscles or scalene.
a = int(input("enter the side 1"))
b = int(input("enter the side 2"))
c = int(input("enter the side 3"))
if a == b == c :
    print("it is an equilateral triangle.")
elif a != b != c :
    print("it is an scalene triangle")       

else:
    print("it is an isoceles triangle")       

#8. Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
# Unit Price
# First 100 units no charge
# Next 100 units Rs 5 per unit
# After 200 units Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs 2000)

unit=int(input("Enter the Number:"))
if unit<=100:
    print("No charges.")
elif 101<=200:
    print("Rs 5 per unit.")
else:
    print("Rs 10 per unit.")

#9. Write a program to accept the cost price of a bike and display the road tax to be
# paid according to the following criteria : 
# Cost price (in Rs)     Tax
# >100000                15 %
# >50000 and <= 100000   10%
# <= 50000               5%

rs=int(input("enter the cost price:"))
if rs>100000:
    print("tax would be 15%.")
elif rs>50000 and rs<=100000:
    print("tax would be 10%")
else:
    print("tax would be 5%")      

#10. Accept the marked price from the user and calculate the Net amount as(Marked
# Price –    Discount to pay according to following criteria:
# Marked Price         Discount
# >10000                 20%
# >7000 and <=10000      15%
# <=7000                 10%

net=int(input("enter the marked price:"))
if net>10000:
    print("20% Discount")
elif net>7000 and net<=10000:
    print("15% Discount")
else:
    print(" 10% Discount")

