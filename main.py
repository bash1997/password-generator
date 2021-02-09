#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password =""

for letter in range(0, nr_letters):
	letter = random.randint(0, len(letters)) #or i could use the random.choice(letters) function
	if letter == len(letters):
		letter -= 1
	password += letters[letter]

for symbol in range(0, nr_symbols):
	symbol = random.randint(0, len(symbols))
	if symbol == len(symbols):
		symbol -= 1
	password += symbols[symbol]

for number in range(0, nr_numbers):
	number = random.randint(0, len(numbers))
	if number == len(numbers):
		number -= 1
	password += numbers[number]

print(f"This is your password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""

for letter in range(0, nr_letters):
	letter = random.randint(0, len(letters))
	if letter == len(letters):
		letter -= 1
	password += letters[letter]
	
for symbol in range(0, nr_symbols):
	symbol = random.randint(0, len(symbols))
	if symbol == len(symbols):
		symbol -= 1
	password += symbols[symbol]

for number in range(0, nr_numbers):
	number = random.randint(0, len(numbers))
	if number == len(numbers):
		number -= 1
	password += numbers[number]

mix_password = "".join(random.sample(password,len(password)))
print(f"Or here is a randomised password: {mix_password}")


## if i used the random.shuffle, password would need to be a list then use the shuffle func then pass each character into a new variable
# password_list = []

# for char in range(1, nr_letters + 1):
# 	password_list += random.choice(letters)
# for char in range(1, nr_symbols + 1):
# 	password_list += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
# 	password_list += random.choice(numbers)
# print(password_list)

# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
# 	password += char
# print(password)