import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_len = len(names) - 1
print(f"{names[random.randint(0, name_len)]} is going to buy the meal today!")