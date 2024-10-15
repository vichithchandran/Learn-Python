# To Read The File
f=open("demo.txt", "r")
data= f.read()
print(data)
f.close()

f=open("demo.txt", "r")
data= f.read(5)
print(data)
f.close()

# Using Readline
f=open("demo.txt", "r")
line1= f.readline()
print(line1)
line2= f.readline()
print(line2)
f.close()

# To Write and Append the file
f=open("demo.txt","w")
f.write(" I want to learn javascript.")
f.close()

f=open("demo.txt","a")
f.write(" \n Then I'll move to React Js.")
f.close()

f=open("smaple.txt", "a")
f.write("This is a simple file")
f.close()


f= open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

f= open("demo.txt","w+")
f.write("abc")
f.close()

f= open("demo.txt","a+")
f.write("abc")
f.close()

# Using with syntax read
with open("demo.txt","r") as f:
  data=f.read()
  print(data) 

 
# Using with syntax write 
with open("demo.txt","w") as f:
  data=f.write("new file")

#remove the file
import os
os.remove("smaple.txt")

# Write to Line
with open("practice.txt", "w") as f:
  f.write("Hi everyone\nWe are learning file I/0\n")
  f.write("Using Java.\nI like programming in java\n")

#Replace Java into Python
with open("practice.txt", "r") as f:
  data=f.read()
new_data= data.replace("Java", "Python")
print(new_data)
with open("practice.txt", "w") as f:
  data=f.write(new_data)

# Check "Learning" word is existing in the file
def check_for_word():
 word="learning"
 with open("practice.txt", "r") as f:
    data= f.read()
    if(word in data):
      print("found")
    else:
      print("not fount")
check_for_word()

# Check for Line
def check_for_line():
    word="programming"
    data=True
    line_no=1
    with open("practice.txt", "r") as f:
        while data:
          data= f.readline()
          if(word in data):
             print(line_no)
             return
          line_no +=1
    return -1     
check_for_line()

# Check even Numeber is existing in the file
count = 0
with open("practice.txt","r") as f:
  data= f.read()

nums= data.split(",")
for val in nums:
  if(int(val) %2 == 0):
    count += 1

print(count)