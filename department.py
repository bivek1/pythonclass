

#Creating a empty list 


# print("\t\t Welcome to Fruits Department")

# # Creating Limit to manipulate data in the department 
# #The limit is user can only add or delete data from department 10 times




user_info = {
    'modal':'2008',
    'color':'black',
    'make_modal':'2007',

}
print(user_info.keys())
print(user_info.values())

for i, j in user_info.items():
    print(i, j)



for i in range(10):
  print("What do you want to insert")
  key_name = input("Enter the key")
  value_nname = input("Enter the value")
  user_info.update(
      {
          key_name:value_nname
      }
  )
  print(user_info)


# user_info.update({
#     'price':'$20000'
# })
# user_info['price'] ='$30000'

# print(user_info['price'])
# print(len(user_info))
# # To get specific key value\
# modal = user_info.get('modal')

# print(modal)

# fruits_list = ['mango','banana']

# while True:
    
    
#     print("Add fruits name to append in the data list or remove from the data list")
#     print("Press 1 to add item and 2 to delete item")
#     choose = input("Choose the option:")
#     item = input("Enter fruits name:")

#     print("You have ",  limit , 'times limit')

#     limit = limit - 1

#     if limit == 0:
#         print("Your limit has been completed for today come back later")
#         break

#     if int(choose) == 1:
#         fruits_list.append(item)
#         print(fruits_list)
#     elif int(choose) == 2:
#         fruits_list.remove(item)
#         print(fruits_list)
