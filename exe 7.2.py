paragraph = input("Enter your paragraph: ")

words = paragraph.lower().split()
count = 0

for word in words:
    if word == "python":
        count += 1

print("\nNumber of times 'python' appears:", count)