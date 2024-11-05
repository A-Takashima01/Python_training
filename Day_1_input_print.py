# print("fun")


# # print -> user -> output
# name = input("Your name: ") # Input -> str
# age = input("Age: ") # Input -> str
# height = input("Height: ") # Input -> str

# print("Hello, ", name,". 🎊")
# print("Your age is", age, "and your height is", height, "cms.")

# # Task
# # Get (name, age, height)
# # Output
# # Hello, Ayane
# # Your age is 26 and your height is 168cms

print("fun")

# Read the data from user
# print -> user -> input 
name = input("Please tell me your name? ") # input -> str
age = input("Please tell me your age? ")  # input -> str
height = input("Please tell me your height? ")  # input -> str

print(type(name))
print(type(age))
print(type(height))



# Display the data to the user
print("Hello,", name, "🎊") # adds <space>

# hello_message =  "Hello,", name, "🎊" # ❌
hello_message =  "Hello, " + name + " 🎊" # ✅

# str1 + str2
# str + int

# print(hello_message)
output = "Your age is " + age + " and height " + height
print(output)



# Task
# 1. Get (name, age, height)
# Output
# Hello, Natsumi 🎊 
# Your age is 20 and height 5.7


# print("No. of fans " +  30) # ❌
# print("No. of fans " +  "30") # ✅

# followers = 30000
# # print("No. of fans " +  followers) # ❌
# # print("No. of fans " +  "followers")  # ❌

# print("No. of fans " +  str(followers))
