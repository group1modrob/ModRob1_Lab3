# Try Except
# try and except can help us handle the expceptions that might occur during execution

# first we define a function called divide_numbers
def divide_numbers(x,y):
    # if there is no error during execution of this code, it will return x/y 
    try:
        return x/y
    # This except handle the zero division error which will happen when the value divide by zero. if ZeroDivisionError occur, it will return the message Division by zero error 
    except ZeroDivisionError:
        return "Division by zero error"
    # This will handle other input error, and return the message invalid 
    except:
        return "Invalid"

# now we can try how the function works
print(divide_numbers(5,2))
print(divide_numbers(0,0))
print(divide_numbers('0',0))