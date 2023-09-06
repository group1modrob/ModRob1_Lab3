# This file goes into Tuples. Tuples are like lists, but they are immutable (you can't modify them!) As an example:
group1 = ("Namrata", "Brayn", "Tai", "Wilfredo")
print("\nA printed tuple looks like this:")
print(group1)

# You also access individual elements in them the same way you would do so in lists
print("\nThe third value in the group1 tuple is:")
print(group1[2])

# You can unpack a tuple and save them as individual elements
member1, member2, member3, member4 = group1
print("\nThe members of this group are: ")
print(member1 + "\n" + member2 + "\n" + member3 + "\n" + member4)
print("\nAnd the third member of the group is:")
print(member3)

# If you try to change anything inside a tuple, you will get an error!
print("\nTrying to change the first element of the tuple...")
try:
    group1[0] = "Madi"
except:
    print("\nERROR: Tuples are immutable!")

# If needed, you can make a list of tuples
groupX = [(group1[3], group1[0]), (group1[2], group1[1])]
print("\nThe new group is:\n" + str(groupX))
print("\nAnd their first pair is:\n" + str(groupX[0]))