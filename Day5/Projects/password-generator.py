import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letter_count = int(input("How many letters would you like in your password?"))
symbol_count = int(input("How many symbols would you like?"))
number_count = int(input("How many numbers would you like?"))

password = ""

for char in range(1, letter_count + 1):
    password += random.choice(letters)

for char in range(1, symbol_count + 1):
    password += random.choice(symbols)

for char in range(1, number_count + 1):
    password += random.choice(numbers)

print(f"Your password is: {password}")