# 2D lists are a somewhat simplistic way of expressing 2D matrices in Python. Other ways for matrix operations will be used later on in the lab! (Numpy Arrays!)
# If you want to look at them as a table, think of each list as a "column" and each element in the list as an element in a "row"
# As an example, let's create a matrix that gives each of the member in this group a random feature.
# The first column is "Group Member", the second is "Height", and the third is "Weight". Since there are 4 lab members (rows), and three categories (Name, Height, Weight, the columns!), then this is a 4x3 table! (it's just one potential interpretation of a 2D list )
table = [["Namrata", "Brayn", "Tai", "Wilfredo"], [160, 170, 190, 180], [100, 200, 200, 300]]
print("The full table is:")
print(table)

# Now if we want to access individual elements in this "table":
# We can access the element in the first row and first column (indices start from 0)
print("\nThe element in the first row, first column is:")
print(table[0][0])

# And another example:
print("\nAnd now in the second column, last row")
print(table[1][3])