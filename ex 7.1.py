email_text = input("Enter the email text: ")

at_count = email_text.count("@")
exclamation_count = email_text.count("!")
hash_count = email_text.count("#")
dollar_count = email_text.count("$")

print("\n--- Email Scanner Result ---")
print("Text:", email_text)
print("@ symbols:", at_count)
print("! symbols:", exclamation_count)
print("# symbols:", hash_count)
print("$ symbols:", dollar_count)

total = at_count + exclamation_count + hash_count + dollar_count

print("Total special symbols:", total)