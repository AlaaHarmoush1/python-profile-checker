print("Hello and Welcom")

name= input("Enter your name:")
age = int(input("Enter your age:"))
gpa = float(input("Enter your GPA:"))
field_of_interest = input("Enter your field of interest:")
graduated = input("Are you graduated? (yes or no): ").lower()


if age <= 25 and gpa >= 3.5 and graduated == "yes":
    print(f"You are eligible for a scholarship in {field_of_interest} field")
elif age < 30 and gpa >= 2.5:
    print(f"You are eligible for an internship ")
else:
    print("apply again later")

