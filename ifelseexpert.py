# Career Path Expert System using if-else

print("Welcome to Career Path Expert System")
print("Answer the following questions with 'yes' or 'no'.")

math = input("Do you like Mathematics? (yes/no): ").lower()
physics = input("Do you like Physics? (yes/no): ").lower()
computers = input("Do you like working with Computers and Programming? (yes/no): ").lower()
chemistry = input("Do you like Chemistry? (yes/no): ").lower()
electronics = input("Do you like Electronics and Circuits? (yes/no): ").lower()

# Career suggestion logic
if math == "yes" and physics == "yes":
    print("Suggested Career Path: Mechanical Engineering")

elif math == "yes" and computers == "yes":
    print("Suggested Career Path: Computer Science Engineering")

elif chemistry == "yes" and math == "yes":
    print("Suggested Career Path: Chemical Engineering")

elif electronics == "yes" and physics == "yes":
    print("Suggested Career Path: Electrical/Electronics Engineering")

elif math == "yes" and physics == "yes" and computers == "yes":
    print("Suggested Career Path: Artificial Intelligence & Data Science Engineering")

else:
    print("Suggested Career Path: General Engineering / Explore More Fields")
# Career Path Expert System using if-else

print("Welcome to Career Path Expert System")
print("Answer the following questions with 'yes' or 'no'.")

math = input("Do you like Mathematics? (yes/no): ").lower()
physics = input("Do you like Physics? (yes/no): ").lower()
computers = input("Do you like working with Computers and Programming? (yes/no): ").lower()
chemistry = input("Do you like Chemistry? (yes/no): ").lower()
electronics = input("Do you like Electronics and Circuits? (yes/no): ").lower()

# Career suggestion logic
if math == "yes" and physics == "yes":
    print("Suggested Career Path: Mechanical Engineering")

elif math == "yes" and computers == "yes":
    print("Suggested Career Path: Computer Science Engineering")

elif chemistry == "yes" and math == "yes":
    print("Suggested Career Path: Chemical Engineering")

elif electronics == "yes" and physics == "yes":
    print("Suggested Career Path: Electrical/Electronics Engineering")

elif math == "yes" and physics == "yes" and computers == "yes":
    print("Suggested Career Path: Artificial Intelligence & Data Science Engineering")

else:
    print("Suggested Career Path: Explore More Fields")
