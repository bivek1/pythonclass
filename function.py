# #There are two types of function i.e. Inbuilt function and user defined function
# #Example of inbuilt function are: print(), len(), count(), inpurt(), lower()


# #Example of user defined function
# def myFunction(): #here myFuncation is a name of funcation
#     print("This is function")

# myFunction()



# #How to perform calculation within function
# #Example of function calculating somthing with any parameter
# def calculate():
#     num1 = 34
#     num2 = 55

#     multiply = num1 * num2

#     print(multiply)

# # To call the above calculation we call the funcation 
# calculate()



# #How to return any operation from function 
# def returingFunction():
#     num1 = 30
#     num2 = 200

#     return num1+num2

# return_data = returingFunction()
# print(return_data)

# num2 = 22
# #How to send parameter as an argument of function and perform operation
# def parameterFunction(num1, num2, num3, name):
#     print(num1)
#     print(num2)
#     print(num3)
#     print(name)

# # Sending parameter to function 
# num1 = input("Enter number 1: ")
# parameterFunction(num1, 40, 70, 'Ram')


# #How to perfrom operation inside function using parameters
# def paraFunction(naming, year):
#     print("The user name is", naming)
#     current_year = 2024
#     real_age = current_year - int(year)

#     return real_age


# name = input("Enter your name: ")
# age = input("Enter your age: ")

# real_birth_year = paraFunction(name, age)

# print("Your birth year is", real_birth_year)


#How to handle arbitary arguments 
def arbiFuntion(*args):
    #This is in tuple form
    print(args)
    selected_user = ['Ram', 'Raj']
    for i in args:
        print(i)
        if i in selected_user:
            print("Selected user arugment found ", i)


arbiFuntion("Ram", "Sam", "Hari", "Sita","Bibek", "Raj", "Gita", "Sunita", "Rajesh")



#How to handle keyword agruments 
def kwFunction(**kwargs):
    # It is in dictionary form
    print(kwargs) 

kwFunction(name1 = "Ram", name2= "Sam", name3 = "Ramesh")


#Default Value function
def defaultValueFunction(country = "Nepal", city = "Kathmandu"):

    print("Your country is ", country)
    print("Your city is ", city)

defaultValueFunction(country= "Japan")


#How to define and access global variable 
street = "Jorpati"

def globalchangeFuncation():
    global street
    street = "Chabel"
    print(street)

globalchangeFuncation()

print(street)