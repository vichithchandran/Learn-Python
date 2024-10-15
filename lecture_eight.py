# class Student:# Class
#   name="karan"
# s1 = Student() #Object
# print(s1.name)

# class Car:
#   color ="blue"
#   brand ="Mercedes"
# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Student:

#   #default constructors
#   def __init__(self): 
#    pass

#   #parameterized constructors
#   def __init__(self, name,marks): 
#     self.name = name
#     self.marks =marks
#     print("Adding new student in database...")

# s1 = Student("Karan",97) 
# print(s1.name, s1.marks)

# s2 = Student("Arjun",98) 
# print(s2.name, s2.marks)

# class Student:
#   college_name ="ABC College"
#   name="annymous" #class attr
#   def __init__(self, name,marks): 
#     self.name = name # obj attr > class attr
#     self.marks =marks
#     print("Adding new student in database...")

# s1 = Student("Karan", 97) 
# print(s1.name, s1.marks)

# s2 = Student("Arjun", 98) 
# print(s2.name, s2.marks)
# print(Student.college_name)

# class Student:
#   college_name ="ABC College"
  
#   def __init__(self, name,marks): 
#     self.name = name 
#     self.marks =marks
  
#   def welcome(self): #Method
#     print("Welcome Students,", self.name)

#   def get_marks(self): #Method
#     return self.marks

# s1 = Student("Karan", 97) 
# s1.welcome()
# print(s1.get_marks())

# To find the average of marks using constructor
# class Students:
#   def __init__(self, name, marks):
#     self.name =name
#     self.marks=marks

#   def get_avg(self):
#     sum = 0
#     for val in self.marks:
#       sum+=val
#     print("hi", self.name, "your avg score is:", sum/3 )


# s1= Students("Tony Strak", [99,98,97]) 
# s1.get_avg()

# s1.name="iron man"
# s1.get_avg()

#static method
# class Students:
#   def __init__(self, name, marks):
#     self.name =name
#     self.marks=marks

#   @staticmethod #decorator
#   def hello():
#     print("hello")  

#   def get_avg(self):
#     sum = 0
#     for val in self.marks:
#       sum+=val
#     print("hi", self.name, "your avg score is:", sum/3 )


# s1= Students("Tony Strak", [99,98,97]) 
# s1.get_avg()
# s1.hello()
 
# class Car:
#   def __init__(self):
#     self.acc = False
#     self.brk = False
#     self.clutch = False
  
#   def start(self):
#     self.clutch =True
#     self.acc =True
#     print("car Started ...")  
# car1 = Car()
# car1.start()    

# Debit and Credit of bank account
# class Account:
#   def __init__(self, bal, acc):
#     self.balance =bal
#     self.account_no = acc

#   def debit(self, amount):
#     self.balance -= amount
#     print("Rs.", amount, "was debited")
#     print("total balance =",self.get_balance())

#   def credit(self, amount):
#     self.balance += amount
#     print("Rs.", amount, "was credited")
#     print("total balance =",self.get_balance())

#   def get_balance(self):
#     return self.balance

# acc1 = Account(10000, 12345)    
# acc1.debit(1000)
# acc1.credit(500)

# class Student:
#   def __init__(self,name):
#     self.name =name

# s1 = Student("shradha")
# print(s1.name)
# del s1.name
# print(s1.name)

# class Account:
#   def __init__(self, acc_no, acc_pass):
#     self.acc_no =acc_no
#     self.__acc_pass = acc_pass #private

#   def reset_pass(self):
#     print(self.__acc_pass)  

# acc1 = Account("12345","abcde")  

# print(acc1.acc_no)  
# print(acc1.reset_pass())  

# class Person:
#   __name ="anonymous" #private

#   def __hello(self): #private
#     print("hello person!")

#   def welcome(self):
#     self.__hello()  

# p1=Person()
# print(p1.welcome())


# single Inheritance
# class Car:
#     color ="black"
#     @staticmethod
#     def start():
#         print("car started.")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name =name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.color)

#multiple levle inhertance
# class Car:
#     @staticmethod
#     def start():
#         print("car started.")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.name =brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")        
# car1.start()

# #multiple inheritance
# class A:
#   varA = "welcome to class A"

# class B:
#   varB = "Welcome to class B"

# class C(A,B):
#   varC = "Welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# # class method
# class Person:
#   name = "anonymous"

#   # def changeName(self,name):
#   #   self.__class__.name ="Rahul"

#   @classmethod
#   def changeName(cls, name):
#     cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)

#property method
# class Student:
#   def __init__(self, phy, chem, math):
#     self.phy = phy
#     self.chem = chem
#     self.math = math  

#   @property
#   def percentage(self):
#     return  str((self.phy + self.chem + self.math )/3) + "%"
     
# stu1 = Student(54, 68 , 77)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)

# calculate complex number
class Complex:
  def __init__(self,real,img):
    self.real =real
    self.img=img
  
  def showNumber(self):
    print(self.real,"i +", self.img ,"j" )

  def __add__(self,num2):
    newReal = self.real + num2.real
    newImg  = self.img + num2.img
    return Complex(newReal,newImg)
  
  def __sub__(self,num2):
    newReal = self.real - num2.real
    newImg  = self.img - num2.img
    return Complex(newReal,newImg)

num1 = Complex(1,3) 
num2 = Complex(4,6) 
num1.showNumber()
num2.showNumber()

num3 = num1 + num2
num3 = num1 - num2
num3.showNumber()