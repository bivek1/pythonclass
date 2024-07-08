# # To define class we use class and its name 
import math
# class MyCollege:
#     x = "Ram"

# obj = MyCollege()
# print(obj.x)


# # This is how we create class with constructor
# class ClassWithCons:
#     def __init__(self):
#         print("This is being called when initizating object")

# obj1 = ClassWithCons()


# # This is how we pass parameter(data) to class
# class ClassWithData:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#         print(self.name)
#         print(self.address)

# obj2 = ClassWithData('Bibek', "Jorpati")

# This is how we add multiple function in a class
# class mutipleFunctionClass:
#     def __init__(self,name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def printName(self):
#         print(self.name)

#     def printAge(self):
#         print(self.age)

#     def printAddress(self):
#         print(self.address)

# obj3 = mutipleFunctionClass('Sunil', 34, 'Chabel')
# obj3.printName()
# obj3.printAge()
# obj3.printAddress()


# Making simple calulator using class 
class Calculator:
    def __init__(self, num):
        self.number = num
        self.splited_data = None
        self.total_amt = 0
        print(self.number)
    
    def sumFunction(self):
        self.total_amt = int(self.splited_data[0]) + int(self.splited_data[1])
        print(self.total_amt)

    def subFunction(self):
        self.total_amt = int(self.splited_data[0]) - int(self.splited_data[1])
        print(self.total_amt)

    def multiplyFunction(self):
        self.total_amt = int(self.splited_data[0]) * int(self.splited_data[1])
        print(self.total_amt)

    def divideFunction(self):
        self.total_amt = int(self.splited_data[0]) / int(self.splited_data[1])
        print(self.total_amt)

    def sqrShow(self):
        print(self.total_amt)

    def splitFunction(self):
        if '+' in self.number:
            print(self.number.split("+"))
            self.splited_data = self.number.split("+")
            print(self.splited_data)
            self.sumFunction()

        elif '-' in self.number:
            self.splited_data = self.number.split("-")
            self.subFunction()
        
        elif "*" in self.number:
            self.splited_data = self.number.split("*")   
            self.multiplyFunction()
        
        elif '/' in self.number:
            self.splited_data = self.number.split("/")  
            self.divideFunction() 

        else:
            self.total_amt = math.sqrt(int(self.number))
            self.sqrShow()



while True:
    print("Please Enter exit to exit if you want:")
    user_input = input("Enter a number to calulate")
    if user_input == "exit":
        break
    else:
        obj4 = Calculator(user_input)
        obj4.splitFunction()


# # Inheritance in class
# class ParentClass:
#     def __init__(self, name):
#         self.name = name
#         self.class_type= "BSCIT"
#         print("This is parent class")

#     def printName(self):
#         print(self.name)


# # Here we are inherting the parent class
# class ChildClass(ParentClass):
#    pass

# obj1 = ChildClass("Bibek")
# print(obj1.class_type)
# obj1.printName()

# Class Parent2

# class Parent2:
#     def __init__(self, name, address) -> None:
#         self.name = name
#         self.address = address

#         print("This is being called from parent class")
#         print(f"{self.name} {self.address}")


# class Child2(Parent2):
#     def printNumber(self):
#         print("This is number")

# obj3 = Child2("Bibek", "Bouddha")
# obj4 = Child2("Ram", "Sinduli")
# obj5 = Child2("Sam", "Chabel")
