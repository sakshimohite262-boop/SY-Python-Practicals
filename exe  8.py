#=====================================================
# CUSTOMER FEEDBACK FORMATTER
# Teaching : Built-in String Methods &string Formatting
#======================================================

#Step 1: Input raw customer data 
raw_name = input("Enter customer name: ")
raw_feedback = ("Enter feedback message: ")
rating = input("Enter rating (1 to 5): ")

#-----------------------------------------------------
# CONCEPT 1: BUILT-IN STRING METHODS
#-----------------------------------------------------

# 1.   .strip() remove unwanted spaces from the start and  end 
clean_name = raw_name.strip()
claen_feedback =raw_feedback()

# 2.    .title() capitalise the first letter of each word
formatted_feedback = clean_name.title()

# 3.    .capitalise() makes only the vary first leeter of the message uppercase
formatted_feedback = claen_feedback.capitalise()

# 4.    .replace() repalce specific words or characters 
formatted_feedback = formatted_feedback.replace("u","you").replace("r","are")

# 5.      .counts() count occurrences of a specific character 
exclamation_count = formatted_feedback.count("!")

# 6.      .upper() converts to texts to ALL CAPS for important tags
while True:
    if (rating>=1 and rating<=5):
        if int(rating) >= 4:
            category = "POSITIVE".upper()
        else:
            category = "NEEDS REVIEW".upper()
        break
    else:
        resting = int(input("invalid rating provided .Enter rating (1 to 5): "))

#---------------------------------------------------------------------
# CONCEPT 2:STARTING FORMATING (f-string)
#--------------------------------------------------------------------

# Display formated report using f-string and text alignment
print("\n"+"="*45)
# :^45 centers the text within a 45-character wide block
print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}") 
print("-"*45)

#Standard f-string variable interpolation
print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} /5 Stars ")
print(f"Category      : [{category}]")
print(f"Excitement    : {exclamation_count} exclamation mark(s)")
print("-" * 45)
print("Formatted Message :")
print(f'"{formatted_feedback}"')
print("-" * 45)

         



