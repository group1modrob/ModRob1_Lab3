# in this example we want to write a function that gives us the minimum number of three numbers that we pass to it

# first we define a function called "min_num" 
def min_num(a,b,c):
    #There are 4 conditions for this function.
    #The first condition is about a being the smallest number. If it matches, it will return "The smallest number is a"
    if a < b and a < c:
        return "The smallest number is " + str(a)
    # This conidtion is about b being the smallest number. If the conidtion matches, it will return "The smallest number is b"
    # If the function does not match this condition, it will then attempt the following conditions
    elif b < a and b < c:
        return "The smallest number is " + str(b)
    # This conidtion is about c being the smallest number. If the conidtion matches, it will return "The smallest number is c"
    # If the function does not match this condition, it will then attempt the following conditions
    elif c < a and c < b:
        return "The smallest number is " + str(c)
    # If the function doesn't match all the previous conditions, it will return "They are equal"
    else:
        return "They are equal"
    

# now we can try how the function works with all the conditions we set
print(min_num(-2,-1,0))
print(min_num(0,-4,1))
print(min_num(-1,-2,-6))
print(min_num(-0.5,-0.5,-0.5))