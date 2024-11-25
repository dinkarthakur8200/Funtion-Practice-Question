    #                     Query -1
# # You are given a temperature in Celsius. Your task is to convert it to Fahrenheit and return the result.

# Formula:

# To convert Celsius to Fahrenheit, use the formula:

# F = (9/5 * C) + 32

# Where F is the temperature in Fahrenheit and C is the temperature in Celsius.

def celsius_to_fehreneit(celsius):
     fahrenheit = (9/5*celsius)+32
     return fahrenheit
celsius_input = float(input("Enter the temperature in Celsius : "))
fahreneit_result = celsius_to_fehreneit(celsius_input)
print(f"The temperature in Fahreneit is : {fahreneit_result}");

