

# def message():  #define function
#     print('hello') #hello
# message()   #calling function #hello
# print(message())    #none

# def message(name):
#     print('Hello',name)
# message('students')    

# def message(name,period):
#     print('hello',name)
#     print('good',period)
# message ('sneha','night')
# message (period='morning',name='sahil')

# def message(name,period = 'evening'):
#     print('hello',name)
#     print('good',period)

# message('sachin','afternoon')    

# def sum(*numbers):
#     s=0
#     for n in numbers:
#         s=s+n
#     print("sum of" , numbers,"=" , s)        
# sum(1,2,3)

# def sum(*numbers):
#     s=0
#     for n in numbers:
#         s=s+n
#     print("sum of" , numbers,"=" , s) 
# sum(1,2,3,4,5,6,7,8,9)    
# sum(6.99,5.88,3.67)
# sum()

# def sum(a,b):
#     c=a+b
#     return c
# print('sum of 5 and 6=',sum(5,6))

# ans=sum(5,6)
# print('sum of 5 and 6=',ans)
#write a program accept numbers from users until user want them to take sum and then calculate average
# number = int(input("Enter a number: "))
# total_sum = sum(range(1, number + 1)) 
# print(f"The sum of all numbers from 1 to {number} is {total_sum}.") 

# G1=10
# def sample(n):
#     L1=10
#     L1=L1+n+G1
#     print(L1)

# sample(10)
# print("Global Variable",G1) 
# print("local Variable",L1)  

# def calculator(a,b):
#     def addition(a,b):
#         return a+b
#     def substraction(a,b):
#         return a-b
#     def multiplication(a,b):
#         return a*b
#     def division(a,b):
#         return a/b            

#     print("Addition :",addition(a,b))
#     print("Substraction :",substraction(a,b))
#     print("Multiplication :",multiplication(a,b))
#     print("Division :",division(a,b))

# calculator(40,10)

# def calculator(a,b):
#     def addition(a,b):
#         return a+b
#     def substraction(a,b):
#         return a-b
#     def multiplication(a,b):
#         return a*b
#     def division(a,b):
#         return a/b   
#     add,sub,mul,div=addition(a,b),substraction(a,b),multiplication(a,b),division(a,b)
#     return add,sub,mul,div

# print(calculator(40,10))      

# G1=10
# G2=20
# def sample(n):
#     L1=0
#     global G2
#     G2=20
#     L1=L1+n+G1+G2

# sample(10)
# print("Global Variable",G1)
# print("Global Variable within Function",G2)
# # Print("local variable",L1)     

# a=20

# def scopedemo():
#     global a
#     a=10
#     print("a=",globals()['a'])
#     print("a=",a)
# scopedemo()    

#recurssion is the process where function called itself from its own body (define recurrsion)


# def SayHello(name):
#     print("Hello {}! How are you?".format(name))
#     return
# import Hello
# hello.sayhello("abc")
#print(hello._name_)

# L1=[]
# type(L1)
# print(type(L1))
# L2=list([1,2,3,4,5])
# print(L2)
# print(L2[3])
# print(L2[-3])
# print(L2[2:4])
# L3=['s','n','e','h','a']
# print(L3)
# L4=[101,'ajay',"ajay@gmail.com",76567.78]
# print(L4)
# class sample:
#     c=0   #class variable
# def __init__(self):
#     self.n=int(input("enter the value")) #instance variable
# def display(self):
#     print("number",self.n)
# def __del__(self):
#     print("object destroyed")    

# obj1=sample()
# obj2=sample()
# print("object1")
# obj1.display()
# print("object2")
# obj2.display()

# class constr_types:
#     def__init__(self):
#     print('default constructor')
#     data=arg1
#     print("parametrised constructor")
# obj1=constr_types()
# obj2=constr_types(10) 

#create a class to store a details of 5 students and display it (use array or list)
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# class StudentRecords:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def display_students(self):
#         for student in self.students:
#             student.display()

# records = StudentRecords()
# records.add_student(Student("Alice", 20, "A"))
# records.add_student(Student("Bob", 21, "B"))
# records.add_student(Student("Charlie", 19, "A"))
# records.add_student(Student("David", 22, "C"))
# records.add_student(Student("Eve", 20, "B"))
# print("Student Details:")
#records.display_students()

# class derive-class(<base class1>,<base class2>,......<base class n>):
#     <class-suite>

# class vehicle:
#     def __init__(self):
#         self.make=''
#         self.model=''
#     def DisplayDetails(self):
#         print("make :",self.make,"\nModel :",self.model)

# class swift(vehicle):
#     def __init__(self):
#         self.make='hundai'
#         self.model='v2'

# o2=swift()
# o2.DisplayDetails()               

print(isinstance(fy_std1,fy))
print(isinstance(fy_std1,sy))
print(isinstance(fy_))
build a class object having attribute 