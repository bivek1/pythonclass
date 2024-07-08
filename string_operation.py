# p = "This is string it's"
# name = 'hello Student'
# print(p)
# print(len(p))
# print(name)

# a = "Hello, World!"
# print(a[6])

# for i in a:
#     print(i)


# email = input('Enter your email:')


# # Checking if the value is not presented in given string
# if '@' not in email:
#     print("Email not valid")
# else:
#     print("Email validated succesfully")


example = "Favourite food is mango"

# # Checkong if a value present in string
# if 'mango' in example:
#     print("Yes mango is fav")


# Slicing in string 
print(example[2:8])

# slicing getting from last indexing
print(example[-1])

# slicing without denoting begining index
print(example[:10])

#This slicing will give all value from given begining indexing to last
print(example[10:])

b = "Hello, World!"
print(b[-5:-2])

# Modifying String 
sentence = "The World is Beautiful so lets be HAPPY"

# To make all element inside string into lowercase
print(sentence.lower())

#To make all element inside string into uppercase
upper_sentence = sentence.upper()

print(upper_sentence)


# Removing whitespace from the string
# Whitespace means unwanted space in the sentence
new_sentence = "  Texas college of Management and IT  "
print(new_sentence.strip())

# To replace anything charecter and a word from a string we use replace
school = new_sentence.strip().replace('college', 'school')
print(school)
print(len(school))

# Splitting the string
split_name = "Rajesh!Hamal"
print(split_name.split('!'))
print(type(split_name.split('!')))

# String Concatination (JOINING THE STRING)
first_name = "Bibek"
last_name = "Dhakal"

concate_name = first_name+"    "+last_name
print(concate_name)
print(first_name+" "+last_name)


def sum(a,b):
    su = a+b
    return su

sum_amt = sum(10, 20)
print(sum_amt)

def minus(a,b):
    su = a-b
    return su

sub_amt = minus(50, 20)
print(sub_amt)
# There is two way of formating string and variable
print("The sum of 10 and 20 is", sum_amt, "The subtract of 50 and 20 is", sub_amt)
print("The sum of 10 and 20 is " + str(sum_amt))

print(f"The sum of 10 and 20 {sum_amt}")

print(f"{sum_amt} is the total sum")

# We can perfom any arthematic operation within {} while formating string 
print(f"{4*10} is multply value of 4 and 10")


print("Laxmi prasad devkota wrote \"muna madan\" ")


name = "Ram is best man"
if name.startswith("Ram"):
    print("yes ram is there")


