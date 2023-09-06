# to read this file, we should first open it

with open("sensor_data.txt", "r") as servo1_sensor_data:
    # now iterate over each line
    for info in servo1_sensor_data:
        # get rid of spaces in between and split the line into date, time, temperature, latitude and longitude position:
        date, time, temperature, lat, long, = info.strip().split("*")

        # now we can process the data
        print("Date: ", date)
        print("Time: ", time)
        print("Temperature: ", temperature)
        print("Latitude: ", lat)
        print("Longitude: ", long)
        
