age = int(input("Age: "))
income = int(input("Income: "))
caste = input("Caste (SC/ST/OBC/NT/General): ").upper()

if age < 25:
    if income < 300000:
        if caste in ["SC", "ST", "OBC"]:
            print("Scholarship Approved")
        else:
            print("Caste criteria not met")
    else:
        print("Income limit exceeded")
else:
    print("Age limit exceeded")