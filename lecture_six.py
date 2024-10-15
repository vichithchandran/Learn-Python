# def sum(a,b):
#   s= a + b
#   return s
# print(sum(2,3))

# def calc_sum(a,b):
#   sum= a + b
#   print(sum)
#   return(sum)

# calc_sum(5,10)
# calc_sum(2,10)
# calc_sum(12,17)

#Function Definition 
# def calc_sum(a, b): #parameter
#   return a +b

# sum =calc_sum(1,2) # function call; arguments
# print(sum)

# def print_hello():
#   print("hello")

# print_hello()
# print_hello()
# print_hello()

#avgerage of 3 numbers
# def cal_avg(a, b, c):
#   sum = a + b + c
#   avg  = sum / 3
#   print(avg)
#   return(avg)

# cal_avg(2,3,4)
# cal_avg(98,97,95)

# print("apanacollege", end ="$")
# print("shradhakhapra")

# def calc_prod(a = 1, b =1): # default parameter
#   print(a * b)
#   return a * b
# calc_prod()

# def calc_prod(a,b=2):
#    print(a * b)
#    return a * b
# calc_prod(1)

# q1) print the lenght of the list
# cities = ["delhi", "gurgaon", "nodia", "pune", "mumbai" , "chennai"]

# heroes =["thor", "ironman", "captain america", "shaktiman"]
# def print_len(list):
#   print(len(list))

# print_len(cities)
# print_len(heroes)

# q2) Print the elements of a list in a single line 
# cities = ["delhi", "gurgaon", "nodia", "pune", "mumbai" , "chennai"]

# heroes =["thor", "ironman", "captain america", "shaktiman"]
# def print_len(list):
#   print(len(list))

# def print_list(list):
#   for item in list:
#     print(item, end=" ")

# print_list(heroes)

# q3) find the factorial of n
# def calc_fact(n):
#   fact=1
#   for i in range(1,n+1):
#     fact*= i
#   print(fact)

# calc_fact(5)

# q4) convert usd int inr
# def converter(usd_val):
#   inr_val = usd_val * 83
#   print(usd_val,"USD =", inr_val, "INR")
# converter(120)

# def check_odd_even():
#   num=int(input("Please Enter the number:"))
#   if num % 2 == 0:
#     print(num,"is Even Number")
#   else:
#     print(num,"is Odd Number")
# check_odd_even()    

#recursive Function
# def show(n):
#   if (n == 0):
#     return
#   print(n)
#   show(n-1)
# show(5)  

# def show(n):
#   if (n == 0):
#     return
#   print(n)
#   show(n-1)
#   print("End")
# show(3)  

def fact(n):
  if(n == 0 or n == 1 ):
    return 1
  else:
    return n* fact(n-1)

print(fact(5))

def calc_sum(n):
  if( n == 0):
    return 0
  return calc_sum(n-1) + n
sum = calc_sum(5)
print(sum)


def print_list (list, index=0):
  if(index == len(list)):
     return 
  print(list[index])
  print_list(list, index+1)

fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)