# First we will create two different types of numbers: integers (ints) and floats. Ints have no decimal spaces, floats can have up to 7 decimal digits
int_example = 100
float_example = 0.2

# When printing things to the console, we technically cannot put Strings and Numbers in the same print statement
# The numbers and any other variable type need to be changed to String before being used in the statement
# You do that with the str() command and whatever is given as an argument will be changed to a string
print("My first example was an integer with a value of " + str(int_example) + ".\nThe second example is a float with the value of " + str(float_example) + ".") 

# Another type of variable are String variables. Here I will create an example:
example_string = "Here is an example"
# And now I can use it directly in a print statement because it is already a String
print("\nMy string example will contain the word example because I am a redundant person: " + example_string + ".")

# A list is a variable type that can contain many values OR variables in it. For example, we can create a list of Strings:
example_list = ["Here", "is", "an", "example", "list"]

# We can then print this list
print("\nThe example list is:")
print(example_list)

# We can access individual elements of the list using indexing with []. For example, printing the first element in the list (index starts at 0)
print("\nThe first string in my list is: " + example_list[0])

# We can also use indexing to print all the elements UP TO index X. If I want to print the first 4 elements (index 0 - 3)
# print the first three items in the list
print("\nUp to index = 3 of the list:")
print(example_list[:4]) # Not inclusive of the index listed here

# We can append elements to the list as needed using the .append command
example_list.append("and it could be the final one.")
print("\nAdding an element to the list:")
print(example_list)

# We can remove the big element we just added by using the remove command
example_list.remove("and it could be the final one.")
print("\nAnd now we remove it:")
print(example_list)

# We can insert elements into a specific index in the list
example_list.insert(4, "of a")
print("\nList with a new element inserted:")
print(example_list)

# We can sort in place all the elements in ascending order using the sort() function
example_list.sort()
print("\nSorting the list. Good luck making sense of the original 'sentence' now!")
print(example_list) # And now the sentence will not make any sense

# We can reverse the order of the elements in the list
example_list.reverse()
print("\nReversing the list. Oof, now it will really not make much sense!")
print(example_list) # And now the "sentence" will make less sense :). Organizing it properly would require some code writing! 

# If we want to know the length of the list (how many elements the list has)
print("\nThis list has this number of elements:")
print(len(example_list))

# And we can also append elements from another list to our original list
print("\nExtend the new list by adding all the elements from another list:")
list_to_append = ["Namrata", "Brayn", "Tai", "Wilfredo"]
example_list.extend(list_to_append)
print(example_list)

# To get rid of the last element in the example_list
# we want to get rid of the last element of the robot_brands list
print("\nNow we remove the last element from the list:")
example_list.pop()
print(example_list)

# We can obtain the index of a specific value
print("\nWhat is the index of the element Brayn?")
print(example_list.index("Brayn"))

# We can check how many instances of an element are in a list
print("\nHow many instances of Brayn are there in the list?")
print(example_list.count("Brayn"))

# We can make a copy of a list
print("\nMaking a copy of the list and printing both:")
example_list_2 = example_list.copy()
print(example_list)
print(example_list_2)

# We can iterate through elements in a list with FOR loops (more into them in another code file!)
print("\nPrinting all the elements in the list:")
for element in example_list:
    element_index = example_list.index(element)
    print("The element in index " + str(element_index) + " is: " + element)

# And finally, we can clear a list of everything in it
example_list.clear()
example_list_2.clear()
print("\nHere we make sure the lists have been cleared:")
print(example_list)
print(example_list_2)