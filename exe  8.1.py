# =====================================================
# CUSTOMER FEEDBACK FORMATTER
# Teaching: Built-in String Methods & String Formatting
# =====================================================

# Step 1: Input raw customer data
raw_name = input("Enter customer name: ")
raw_feedback = input("Enter feedback message: ")
rating = int(input("Enter rating (1 to 5): "))

# -----------------------------------------------------
# CONCEPT 1: BUILT-IN STRING METHODS
# -----------------------------------------------------

# 1. .strip() removes unwanted spaces
clean_name = raw_name.strip()
clean_feedback = raw_feedback.strip()

# 2. .title() capitalizes the first letter of each word
formatted_name = clean_name.title()

# 3. .capitalize() makes the first letter uppercase
formatted_feedback = clean_feedback.capitalize()

# 4. .replace() replaces specific words or characters
formatted_feedback = formatted_feedback.replace("u", "you").replace("r", "are")

# 5. .count() counts occurrences of a specific character
exclamation_count = formatted_feedback.count("!")

# 6. .upper() converts text to ALL CAPS
while True:
    if 1 <= rating <= 5:
        if rating >= 4:
            category = "POSITIVE".upper()
        else:
            category = "NEEDS REVIEW".upper()
        break
    else:
        rating = int(input("Invalid rating provided. Enter rating (1 to 5): "))

# -----------------------------------------------------
# CONCEPT 2: STRING FORMATTING (f-string)
# -----------------------------------------------------

print("\n" + "=" * 45)
print(f"{'PROFESSIONAL FEEDBACK REPORT':^45}")
print("-" * 45)

print(f"Customer Name : {formatted_name}")
print(f"Rating        : {rating} /5 Stars")
print(f"Category      : [{category}]")
print(f"Excitement    : {exclamation_count} exclamation mark(s)")
print("-" * 45)

print("Formatted Message :")
print(f'"{formatted_feedback}"')

print("-" * 45)
