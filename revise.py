# ##########################
# # 1. Variable 
# # 2. Data Type
# # 3. Condition
# # 4. Loop 
# # 5. list
# # 6. Dictionary 
# # 7.tuple
# # 8. Set
# # 7. Function


# ##########################
# # name = "Bibek Dhakal"
# # print(type(name))


# #How to identify the given number is odd or even 
# # num1 = input("Enter a number:")
# # print(num1)


# # if int(num1)%2 == 0:
# #     if int(num1) < 100:
# #         print("Given number is less than 100")
# #     print("This number is even")
# # else:
# #     print("This number is odd")


# # Loop 
# # for i in range(1,1000):
# #     if i == 300:
# #         print("I have got 300")
# #         break
# #     print(i)


# # for i in range(1, 10):
# #     print(i, end="")

# # num = 5
# # for i in range(1,num+1):
# #     for j in range(i):
# #         print("*", end="")
# #     print()


# # LIST IN PYTHON
# number_list = [3, 4, 5, 10, 20, 56] #number in list

# # String in list
# # fruit_list = ['Mango', 'Orange', 'Apple', 'Banana', 'Grapes', 'Watermelon', 'Pineapple', 'Guava', 'Papaya', 'Cheery']

# # fruit_list.remove('Guava')


# # print("New list after removing Fruits")

# # print(fruit_list)

# # for i in range(1, 10):
# #     new_fruits = input("Enter new fruits thas has been sold in department:")
# #     if new_fruits == 'exit':
# #         break
# #     fruit_list.remove(new_fruits)
# #     print("Fruits list after removing new item" )
# #     print(fruit_list)



# # while True:
# #     new_fruits = input("Enter new fruits brought in department:")
# #     fruit_list.append(new_fruits)
# #     print("Fruits list after adding new item" )
# #     print(fruit_list)

# # if 'Mango' in fruit_list:
# #     print("Yay there is mango")


# # print(number_list[0])
# # print(fruit_list[2])


# #List Comprehension 
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits[1] ='aaa'
# lisst = [x for x in fruits]
# print(lisst)

# #Sorting list 
# lisst.sort()
# lisst.sort(reverse=True)

# lisst.reverse()


# #List Copy
# new_list = fruits.copy()
# print(new_list)

# print(new_list.count('banana'))

# # Joining list 
# lia1 = [1,2,3,4]
# lia2 = [4,4,12,4]

# print(lia1+lia2)

# lia2.pop(2)

# print(lia2)

# # tuples

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# #SET
# myset = {"apple", "banana", "cherry"}

# #Duplicate are not allowed in set
# # True and 1 is considered the same value:

# thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset)


# # Add an item to a set, using the add() method:

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.remove("banana")

# thisset = {"apple", "banana", "cherry"}

# thisset.discard("banana")

# print(thisset)


# # Join set1 and set2 into a new set:

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1.union(set2)
# print(set3)


# # Use | to join two sets:

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}

# set3 = set1 | set2
# print(set3)


# # Join multiple sets with the union() method:
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1.union(set2, set3, set4)
# print(myset)

# # Use | to join two sets:

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)

# # Join a set with a tuple:

# x = {"a", "b", "c"}
# y = (1, 2, 3)

# z = x.union(y)
# print(z)

# # Join set1 and set2, but keep only the duplicates:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)


# # Use & to join two sets:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)


# # Keep all items from set1 that are not in set2:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

# # Dictionary
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])



# # Using the dict() method to make a dictionary:

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# # Keys of dict
# print(thisdict.keys())

# #Value of the dict
# print(thisdict.values)


# # Make a change in the original dictionary, and see that the values list gets updated as well:

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

# # Change the "year" to 2018:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018


# # Update the "year" of the car by using the update() method:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})



# # The pop() method removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


# # The del keyword removes the item with the specified key name:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)





# dist = {
#     'name':'Bibek dhakal',
#     'age':26,
#     'class':'Master'
# }

# print(dist.keys())
# print(dist.values())

# # dist.pop('name')

# # dist.popitem()

# dist.get('name')

# for i in dist:
#     print(dist[i])


# for x,y in dist.items():
#     print(x, y)





# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# name = input("Enter child name:")
# new = myfamily.get(name)
# print(new.get('year'))

# myfamily.update({
#     'child4':{
#         'name':'maya',
#         'year':2002
#     }
# })

# print(myfamily)
# print(myfamily.pop('child1'))


class Car:
    it = "SUANANA"
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        print("I am being called")

        
    def __str__(self) -> str:
        return f"{self.name}"
    
    def calc(self):
        print(f"{self.name} {self.address} is best thing")

c = Car('Ram', 'Sam')
print(c)
c.calc()
c.address = 24
c.calc()
c.name = "hari"
c.calc()

depa = Car("UANA", 'ass')
depa.calc()

del depa.name
depa.name = "ass"
depa.calc()
# print(c.it)


