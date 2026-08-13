marks = float(input("Enter marks: "))
backlog = input("Any active backlogs(yes/no): ")

if marks >= 70 and backlog == "no":
    print("Eligible for placement")
else:
    print("Not eligible for placement")    
