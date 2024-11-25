# Step 1: Define a function
# A function to calculate the area of a rectangle.
def rectangle_area(length, breadth):
    """
    This function calculates the area of a rectangle.
    Formula: Area = length * breadth
    :param length: Length of the rectangle (float or int)
    :param breadth: Breadth of the rectangle (float or int)
    :return: Area of the rectangle (float or int)
    """
    # Step 2: Apply the area formula
    area = length * breadth  # Multiply length and breadth to calculate the area.
    return area  # Step 3: Return the result.

 
# Step 4: Take user input for length and breadth
# Convert the inputs to floats to handle decimal values.
try:
    length_input = float(input("Enter the length of the rectangle: "))  # Input length
    breadth_input = float(input("Enter the breadth of the rectangle: "))  # Input breadth

    # Step 5: Call the function
    # Pass the user inputs to the function and store the result.
    area_result = rectangle_area(length_input, breadth_input)

    # Step 6: Display the result
    print(f"The area of the rectangle is: {area_result}")  # Output the area.

except ValueError:
    print("Invalid input! Please enter numeric values for length and breadth.")
