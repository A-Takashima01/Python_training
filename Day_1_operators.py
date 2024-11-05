# print("Operators")

# # Addition
# print(5 + 3)
# # Subtraction
# print(10 - 2)
# # Multiplication
# print(4 * 2)
# # Division
# print(16 / 2)

# # Modulus
# print(9 % 2)  # 1
# # Exponentiation
# print(2**3)  # 8
# # Floor Division
# print(7 // 2)  # 3.5 -> 3

# Task
# Expected output
# Please tell me the radious of the circle
# Area of circle -> πr2
# π -> 3.14
# Expected Outpt
#  Please tell me the radius of the circle? 2
#  Area of the cirlce 12.56

# user_radious = input("Radious of circle: ")
# radious_square = (float(user_radious)**2)
# π = 3.14
# area_of_circle = (π * radious_square)
# print("Area of the circle: " + str(area_of_circle))

# # Task 1.2 With f string
# print(f"Area of the circle: {area_of_circle}")

# # Task 2: With f-string
# # Fahrenheit to Celcius
# # Please provide your Fahrenheit: 98.6
# # The 98.6°F is 37°C
# # Formula: °C = (°F - 32) × 5/9
# user_fahrenheit = input("Please input the temperture in °F: ")
# Celcius = ((float(user_fahrenheit) - 32) * 5 / 9)
# print(f"The temperature is {user_fahrenheit}°F. That is {round(Celcius, 2)}°C in celcius.")

# snake_case
fahrenheit = float(input("Please input the temperture in °F: "))
celcius = ((fahrenheit) - 32) * 5 / 9
print(f"The temperature is {fahrenheit}°F. That is {round(celcius, 2)}°C in celcius.")
