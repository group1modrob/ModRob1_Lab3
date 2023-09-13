# this example is imagining a robotic system that inherits from the original Robot class but
# with the added changes of now having wheels and more attributes in the __init__ method

# need to import from the inherited class of Robot.py, since this is the base framework for
# new WheeledRobot class
from Robot import Robot

class WheeledRobot(Robot):
    def __init__ (self, name, DOFs, move_type, num_wheels):
        super().__init__ (name, DOFs) # command for inheriting name and DOFs from the Robot 
                                      # class so there is no need for redefining attributes
        self.move_type = move_type # added attribute telling the type of movement
        
        self.num_wheels = num_wheels # new addition of wheel number being added to __init__ 
                                     # that wasn't present in original Robot class

    def move(self):
        print(f"I am a {self.move_type} robot with {self.num_wheels} wheels.")
        super().move() # this should print the message from inherited Robot class