import time
import random

# The move() function simulates the robot's movement
def move(distance):
    print("Driving the robot...")
    # Simulate the time it takes for the robot to move at the particular distance
    time.sleep(1)
    print(f"Robot traveled {distance} miles.")

# The battery_check function simulates checking the power supply level 
def battery_check():
    # Simulating battery level check
    battery_status= random.randint(0, 100)
    return battery_status

# Robot's initial battery percentage
battery_percentage= 100

# Robot will keep moving until the battery level is low
while battery_percentage > 5:  # Simulating that battery percentage level is less than or equal to 5
    # Generate a random distance to drive (simulating real-world driving conditions)
    distance = random.randint(10, 30)
    # Call the mobe() function to drive the robot the randomly generated distance
    move(distance)
    # Power used during the drive
    battery_percentage -= distance

# When the battery percentage becomes low,print that robot needs to stop
print("Battery LOW! Stopping the robot to recharge.")