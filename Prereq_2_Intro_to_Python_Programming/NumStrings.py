from math import * 
import math as m

# Defining Values
num_int = 10 # this is an integer
num_float = 0.5 # this is a float
members = 4 # num of group members

# Basic Arithmitic (+ = addition; - = subtraction; / = division; * = multiplication; ** = raised to the power of)
print("Test arithmetic operation: " + str(num_int*(num_int+num_float)))

# % is the modulus operator, gives the remainder of a division
print("Test modulus operator using int: " + str(num_int % 3))

# max and min commands largest/smallest numbers using a provided comparison
print("Test min/max command using int: " + str(max(num_int,9)))

# abs command for absolute value
print("Test abs command using int: " + str(abs(-num_int)))

# pow gets the 1st input to the power of the second input
print("Test pow command using int: " + str(pow(num_int,2)))

# round rounds a number down or up with 0.50 being the cutoff point to round down (ex: 0.51 rounds up)
print("Test round command using float: " + str(round(num_float)))

# floor returns largest int not greater than input
print("Test floor command using float: " + str(floor(num_float)))

# ceil returns largest int greater than input
print("Test ceil command using float: " + str(ceil(num_float)))

# sqrt command for square root, utilizes math import
print("Test sqrt command using int: " + str(m.sqrt(num_int)))

# combining multiple numbers with strings
print("Combining strings: There are " + str(members) + " group members in group #" + str(ceil(num_float)))

# simplified string writing
print("Simplified: There are",members,"group members in group #",ceil(num_float))

# using string variables
member_name = "Bryan"
print("The factory's name is " + member_name)

# accessing different characters in a string
print("The first character in the member's name is " + member_name[0])
print("The third character in the member's name is " + member_name[2])

# using different functions with strings
print("Printing member name in lowercase: "+member_name.lower())
print("Check if member name is all lowercase: ",member_name.islower())

# we can combine different functions
print("Make member name all uppercase and then check:",member_name.upper().isupper())
print("Print length of member name:",len(member_name))
print("Print characters of member name:",member_name[0:len(member_name)]) 
print("Print index of character B:",member_name.index("B")) 
print("Replace member name with another:",member_name.replace("Bryan", "Wilfredo"))
