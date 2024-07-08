#This is how we define set
set_item = {"Apple", "Mango", "Orange", "Pineapple", "Orange", 1,2,5, False}
print(set_item)

# In programming 0 refers to False value and 1 refers to True value
status= 1
if status:
    print("True value")
else:
    print("False Value")

print(type(set_item))

set_variable = set(("apple", "banana", "cherry"))
print(set_variable)

set_variable.remove("apple")


set_variable.add('Orange')

set_variable.pop()

print(set_variable)

copy_vairable = set_variable.copy()
print(copy_vairable)

# set_variable.clear()

print(set_variable)



