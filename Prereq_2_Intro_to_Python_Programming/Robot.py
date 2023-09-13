# This example demonstrates the base Robot class for WheeledRobot.py and FlyingRobot.py to inherit.
# The simple Robot class allows for two very different robots (wheeled and flying) to be "built" 
# using the same sampling of code, demonstrating the power of classes and inheritance.

class Robot:
    # the __init__ method is a constructor that initializes the robot arm's attributes when an
    # object is created from the class
    def __init__ (self, name, DOFs):
        self.name = name 
        self.DOFs = DOFs

    # introduction method for each inherited robot that will follow the string below
    def introduce(self):
        print(f"I am {self.name}, a {self.DOFs} DOF robot.")
    
    # move method to show styles of movement in inherited robots that will print the string below
    def move(self):
        print("I can move in different ways.")