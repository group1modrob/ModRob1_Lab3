# just like the WheeledRobot class, FlyingRobot inherits from original Robot class and makes
# additions to the __init__ and move methods

from Robot import Robot

class FlyingRobot(Robot):
    def __init__ (self, name, DOFs, move_type, max_altitude):
        super().__init__ (name, DOFs) # same initial inheritance as before
        self.move_type = move_type # added attribute telling the type of movement
        self.max_altitude = max_altitude # added altitude to the __init__
    
    def move(self):
        print(f"I am a {self.move_type} robot with a max altitude of {self.max_altitude}.")
        super().move()