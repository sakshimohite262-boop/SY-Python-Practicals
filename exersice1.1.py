name = input("Enter Student Name: ")
prn = input("Enter PRN: ")
class_name = input("Enter Class: ")

python = float(input("Enter Python Marks: ")) 
maths = float(input("Enter Maths Marks: ")) 
os = float(input("Enter OS Marks: "))


total = python + maths + os
average = total / 3
percentage = (total / 300) * 100

print("\n-----STUDENT SCORECARD-----")
print("Name :",name)
print("PRN :",prn)
print("Class :",class_name)
print("Total :",total)
print("Average :",round(average, 2))
print("Percentage :",round(percentage, 2),"%")

