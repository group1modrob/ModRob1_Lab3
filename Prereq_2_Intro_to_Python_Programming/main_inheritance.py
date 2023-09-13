# The final step of inherited classes, creating the object that will be calling the different classes we created including:
# Robot, WheeledRobot, and FlyingRobot

# only need to call the Wheeled/FlyingRobot since Robot is already inherited by their classes
from WheeledRobot import WheeledRobot
from FlyingRobot import FlyingRobot 

# after creating the object, use dot commands to reference the different inherited functions created in the classes
robot1 = WheeledRobot("Rover", 3, "grounded", 4)
robot1.introduce() # notice how this one comes from original Robot class, whereas .move comes from WheeledRobot.
                   # This allows for multiple "layers" to present without needing to redefine in the most recent level
                   # of classes
robot1.move() 


robot2 = FlyingRobot("DroneX", 6, "aerial", 100)
robot2.introduce()
robot2.move()
