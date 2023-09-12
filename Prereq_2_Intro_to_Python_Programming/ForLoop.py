# this is for the for loops section
# these are very basic and easy examples
# more to come in the classes and objects section

# we can use for loop with strings
# a loop that iterates over each character in the string and prints each character on a separate line
saying="Welcome to Group 1 Members of Modern Robotics"
for x in saying:
    print(x)

# we can also use for loops with other data types like lists
# Here we defined a list called joint_group containing the names of all the joints present in the PincherX100, and then we used a for loop to # iterate through each engineer's name in the list and print each name on a separate line. 

joint_group = ["Joint 1", "Joint 2", "Joint 3", "Joint 4"]
for joint in joint_group:
    print(joint)

# let's do another for loop with the indexes
# Here, we are using a for loop to iterate through the indices of the joint list, and for each index, we are printing both the # index itself and the corresponding element (name of the robotic engineer) from the list.

for index in range(len(joint_group)):
    print(index)
    print(joint_group[index])

# you can loop through a series of numbers or range of numbers
# The range function in Python generates a sequence of numbers starting from the first argument and ending at one less than the second argument. So the numbers generated will be from predefined minimum and maximum.
min=0
max=5
for x in range(min, max):
    print(x)
