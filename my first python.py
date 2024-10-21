name = "sneha"
age = 18
price = 25.99
old = False
books = None 

print(name)
print(age)
print(price)
print()

print("hello world")
print("name :" ,"sneha hande ")
print("fruits name:" , "apple , strawberry, cherry, litchi, pineapple ")

print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(books))

print("my name is :" ,name)
print("i am :" ,age)

# arithmetic operaters (+ , -, %, *, /, **)
a=38
b=45
sum=a+b
print(sum)
diff=b-a
print(diff)
print(a*b)
print(a%b) #modulus is used to find remainder 
print(a**b) #a^b
print(a/b)

s=2
t=4
print(s/t) #after dividing value always comes in the form of FLOAT.
print(s**t)
print(s%t)

#relational operators/comparison operators 
#(==, !=, >, <, >=, <=)
a=80
b=50
print(a==b) #false
print(a!=b) #true
print(a>b) #true
print(a<b) #false
print(a>=b) #true
print(a<=b) #false 

#assignment operators (=, +=, -=, *=, /=, %=, **=)
num = 10
num += 10 #20
print("num :" ,num)

num = 10
num -= 10 #0
print("num : " ,num)

num = 10
num *= 5 #50
print("num :" ,num )

num = 10
num /= 2 #5
print("num : " ,num )

num = 10 
num %= 2 # remainder is 0
print ("num :" , num)

num = 10
num **= 2 #100 a^b
print("num :" ,num )

#logical operators ( and , not, or) 
# so basically these operators work on boolean values i.e True and False.

a = 20
b = 30
print (not (a < b) ) # ~ true :- (FALSE)
print ( a < b ) # true
print ( a > b ) # false 
print (not (a > b)) # ~false :- TRUE

a = 80
b = 50
print ( " and operator : " , (a >= b) and ( b <= a )) # T AND T 
print ( " or operator : " , (a == b) or (a <= b))# F OR F 

# there are two types of conversion in python 
# i.e type conversion and type casting 

a = 4.25
b = 2 
sum = a+b 
print (sum) #6.25
# type coversion is directly done by python for us 
# but type casting is done by us forcefully 

a = int("8") #10
b = 2
sum = a+b
print (sum)

a = str (" sneha ") 
b = str (" hande ")
sum = a+b
print (sum) # sneha hande 

a= "hello"
b= "world"
sum= a+b
print (sum)

name = input("Enter your name: ")
print("welc(ome :" ,name)
age = input("Enter my age :")
print ("my age is :", age)
hobby = input("Enter your hobbies :")
print("my hobbies are :", hobby)
pet =input("Enter your favourite pet :")
print (pet)


val = int(input(" enter some value : "))
print(type(val), val)

num = float(input(" Enter the number :"))
print(type(num) , num)

#practice question
#write a program to input 2 numbers and print their sum.
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
print (" sum =" ,num1 + num2)

#write a program to input side of a square and print its area .
value = int(input("Enter the side of the square :"))
print("area :" , value*value) #value **= value this can also be done 

#WAP to input 2 floating point numbers and print their average .
a = float(input("Enter number 1 :"))
b = float(input("Enter number 2 :"))
print(" average :" , (a+b)/2)

#WAP to input 2 integer numbers ,a & b print true if a>=b if not print false
c = int(input("Enter first number:"))
d = int(input("Enter second number:"))
print(c >= d)


