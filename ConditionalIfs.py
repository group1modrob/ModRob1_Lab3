# in this example we want to write a function that gives us the minimum number of three numbers that we pass to it

def min_num(a,b,c):
    if a < b and a < c:
        return "The smallest number is " + str(a)
    elif b < a and b < c:
        return "The smallest number is " + str(b)
    elif c < a and c < b:
        return "The smallest number is " + str(c)
    else:
        return "They are equal"
    


print(min_num(2,-1,0))