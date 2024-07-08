print("\t \t \t This is Mark Generator")

# Showing user other information about marks 
# generator

# To show anything in written form we use print()

print("\t \t \t Marks Generator created by Texas Student")


# To create it we need to take user marks in each subject

science = input("Enter a marks in Science: ")

math = input("Enter a marks in Math: ")

social = input("Enter a marks in Social: ")

nepali = input("Enter a marks in Nepali: ")

gk = input("Enter a marks in Gk: ")

print("Your marks in total")

# Getting total marks by adding marks of each subjects
total_marks = int(science) + int(math) + int(social) + int(nepali) + int(gk)

# without using concatinate
print("Your total marks is: " , total_marks)

#using concatinate
print("Your total marks is: " + str(total_marks))

# To get percentage of a student we calculate like this
# Total Obtained Marks divided by Total Marks of all subject multiply by 100

total_percentage = total_marks/5 

print("Your total percentage is: ", total_percentage)

# Using If else condition to show division or distinction

if total_percentage >= 80 and total_percentage <= 100:
    print("You have got distinction. Congrats")

elif total_percentage >= 60 and total_percentage <= 79:
    print("You have got first division")

elif total_percentage >= 40 and total_percentage <= 59:
    print("You have got second division")

else:
    print("You are fail")


