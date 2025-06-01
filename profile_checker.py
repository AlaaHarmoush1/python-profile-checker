print("Hello and Welcom")

name= input("Enter your name:")
age = input("Enter your age:")
gpa = float(input("Enter your GPA:"))
field_of_interest = input("Enter your field of interest:")
graduated = input("Are you graduated? (yes or no): ").lower()


if age < 25 and gpa >= 3.5 and graduated == "yes":
    print(f"You are eligibl for a scholarship in {field_of_interest} field")

