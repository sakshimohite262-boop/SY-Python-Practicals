age = int(input("Age:"))
income = int(input("Income:"))

if age < 25:
    if income < 300000:
        print("Scholarship Approved")
    else:
        print("Income limit exceeded")
else:
    print("Age limit exceeded")    
     
