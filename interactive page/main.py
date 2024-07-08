import calculate
import oddeven

print("\t Welcome here please select your option:")
print("\t Choose 1 for odd even and 2 for calculation")

choosen_opt = input("Enter your option:")


if choosen_opt == "1":
    num = int(input("Enter number to find odd even:"))
    old_even_result = oddeven.findOddEven(num)
    if old_even_result:
        print("This number is even")
    else:
        print("This number is odd")

elif choosen_opt == "2":
    num1 = input("Enter number 1: ")
    num2 = input("Enter number 2: ")
    sum_data = calculate.calc(int(num1), int(num2))
    print("The sum is", sum_data)

else:
    print("Option not available")