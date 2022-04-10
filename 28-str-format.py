# str.format = optional method that give users more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))  # {} => untuk format string nya
print("The {1} jumped over the {1}".format(animal, item))  # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

text = "The {} jump over the {}"
print(text.format(animal, item))

################################################################
name = "Fedrian"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

###############################################################
number = 3.14159
print("The number pi is {:.2f}".format(number))  # .2f itu floating untuk menampilkan 2 digit dibelakang koma

number2 = 1000
print("The number is {:,}".format(number2))  # berkoma untuk ribuan
print("The number is {:b}".format(number2))  # binary
print("The number is {:o}".format(number2))  # octa
print("The number is {:X}".format(number2))  # hexa
print("The number is {:E}".format(number2))  # scientific notation
