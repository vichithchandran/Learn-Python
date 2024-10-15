
# Area and Perimeter of Circle
# class Circle:
#   def __init__(self,radius):
#     self.radius = radius

#   def area(self):
#     return (22/7) * self.radius ** 2  

#   def perimeter(self):
#     return 2 * (22/7) * self.radius

# c1 =  Circle(21)
# print(c1.area())
# print(c1.perimeter())

# Employee Details
# class Employee:
#   def __init__(self,role,dept,salary):
#     self.role = role
#     self.dept = dept
#     self.salary = salary
  
#   def showDetails(self):
#     print("Role:", self.role)
#     print("Department:", self.dept)
#     print("Salary:", self.salary)

# class Engineer(Employee):
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     super().__init__("Engineer","IT", "75,000")

# # e = Employee("Developer", "Software", "20,000")

# e = Engineer("Rahul", 40)
# print(e.showDetails())

# Order - Item & Price
# class Order:
#   def __init__(self,item,price):
#     self.item = item
#     self.price = price

#   def __gt__(self, ord2):
#     return self.price > ord2.price 

# ord1 = Order("chips", 20)     
# ord2 = Order("tea", 15)
# print(ord1 > ord2)


a = "Vichith Chandran"

unique = []
repeat = []

for  i in a:
    if i in unique:
        repeat.append(i)
    else:
        unique.append(i)
print(repeat)        

a = "Vichith Chandran"
unique_elements = sorted(list(set(a)))
print(unique_elements)