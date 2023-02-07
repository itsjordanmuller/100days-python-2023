# Write a program that switches the values stored in the variables a and b.

# Don't change the code below
a = input("a: ")
b = input("b: ")
# Don't change the code above

####################################
#Write your code below this line

export_a = a
export_b = b
a = export_b
b = export_a

#Write your code above this line
####################################

# Don't change the code below
print("a: " + a)
print("b: " + b)