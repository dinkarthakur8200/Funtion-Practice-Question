# Distance Covered by a Vehicle
# Problem Description:

# You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

# Formula:

# To calculate the distance traveled by a vehicle:

# Distance=Speed×Time



# Input:

# Two floating-point numbers, speed and time, representing the speed of the vehicle and the time it has been traveling.



# Output:

# A floating-point number representing the distance traveled.



# Example:

# Input: speed = 60, time = 2
# Output: 120.0
 
# Input: speed = 50.5, time = 1.5
# Output: 75.75
def calculate_distance(speed,time):

    distance = speed * time 
    return distance 
try:
    speed_input = float(input("Enter the speed of the Vehicle : "))
    time_input = float(input("Enter the Time of vehicle : "))

    # call the function ;
    distance_result = calculate_distance(speed_input,time_input)

    print(f"The Distance covered by the vehicle is : {distance_result}")

except ValueError:
    print("Invalid input! Please enter numeric values for speed and time.")



