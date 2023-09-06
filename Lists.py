num_int = 10 # this is an integer
num_float = 0.5 # this is a float

# combining numbers with strings
print("There are " + str(num_int) + " arm robots in the factory, "+ str(num_float) + " of them are broken.") 

# using string variables
factory_name = "ABC"
print("The factory's name is " + factory_name)

# list of robot brands
robot_brands = ["ABB", "KUKA", "FANUC", "Omron"]

print(robot_brands)

# access the second robot brand in the above list
print(robot_brands[1])

# print the first three items in the list
print(robot_brands[:3])

# add another manufacturer "UR" to the above list
robot_brands.append("UR")
print(robot_brands)

# remove the manufacturer that we just added
robot_brands.remove("UR")
print(robot_brands)

# insert the manufacturer "UR" to the second index
robot_brands.insert(1, "UR")
print(robot_brands)

# sort() function --> sorts the list in assending order
robot_brands.sort()
print(robot_brands)

# reverse the order of the list
robot_brands.reverse()
print(robot_brands)

# length of the list
print(len(robot_brands))

# we now want to append another list to the robot_brands list
robot_brands_1 = ["Yaskawa", "Staubli"]
robot_brands.extend(robot_brands_1)
print(robot_brands)

# we want to get rid of the last element of the robot_brands list
robot_brands.pop()
print(robot_brands)

# find the index of the value "ABB"
print(robot_brands.index("ABB"))

# now let's find out how many times "ABB" is repeated 
print(robot_brands.count("ABB"))

# we want to make a copy of the robot_brands list
robot_brands2 = robot_brands.copy()
print(robot_brands)
print(robot_brands2)


# we can iterate through a list with a for loop
for robot_brand in robot_brands:
    print(robot_brand)


# we can remove everything in a list with clear function
robot_brands.clear()
print(robot_brands)