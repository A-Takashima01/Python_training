# if... else

# Use indentations by pressing tab key

# x = 10
# y = 4

# # Control flow
# if x > y:
#     print(f"{x} is greater")
# else:
#     print(f"{y} is greater")

# Task
# Get two person name
# Case 1:
# Yuma, Yoshi
# 173cm, 163cm
# Expected
# Yuma is taller than Yoshi by 10cm

# # MY ANSWER
# user_1 = input("User 1, please enter your name: ")
# user_2 = input("User 2, please enter your name: ")

# height_1 = float(input(f"{user_1}, please enter your height: "))
# height_2 = float(input(f"{user_2}, please enter your height: "))

# if height_1 > height_2:
#     print(f"{user_1} is taller than {user_2} by {height_1 - height_2}cms.")
# elif height_1 == height_2:
#     print(f"Both {user_1} and {user_2} have the same height.")
# else:
#     print(f"{user_2} is taller than {user_1} by {height_2 - height_1}cms.")

# # Teacher's Solution
# user_1 = input("User 1, please enter your name: ")
# user_2 = input("User 2, please enter your name: ")

# height_1 = float(input(f"{user_1}, please enter your height: "))
# height_2 = float(input(f"{user_2}, please enter your height: "))
# # Use absolutes
# diff_height = abs(height_1 - height_2)

# if height_1 > height_2:
#     print(f"{user_1} is taller than {user_2} by {diff_height}cms.")
# elif height_1 == height_2:
#     print(f"Both {user_1} and {user_2} have the same height.")
# else:
#     print(f"{user_2} is taller than {user_1} by {diff_height}cms.")


# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm

# From batch1
fav_flavour = "orange"
# Shop
# stock1 = "vanilla"
# stock2 = "green tea"
# stock3 = "lemon"
# stock4 = "chocolate"

# In Operations
stock = ["vanilla", "green tea", "lemon", "chocolate"]

# Clear
print("-" * 20)

# Expected Output
# Yes, we have vanilla in stock
flav_order = input("Please enter your favorite flavor 🍧:").lower()

# # Solution1:
# if flav_order == stock1:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock2:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock3:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock4:
#     print(f"Yes, we have {flav_order} in stock!")
# else:
#     print(f"Sorry, we ran out of {fav_flavour}...")

# # Solution2:
# if (flav_order == stock1) or (flav_order == stock2) or (flav_order == stock3) or (flav_order == stock4):
#     print(f"Yes, we have {flav_order} in stock!")
# else:
#     print(f"Sorry, we ran out of {fav_flavour}...")

# Solution3:
if flav_order in stock:
    print(f"Yes, we have {flav_order} in stock!")
else:
    print(f"Sorry, we ran out of {fav_flavour}...")


# Sorry, we ran out orange


# Case 1:
# Yes, we have vanilla in stock

# Case 2:
# "orange"
# Sorry, we ran out of orange

# From batch2
# # Read from the User
# fav_flavour = "vanilla"

# # Shop
# stock1 = "chocolate mint"
# stock2 = "vanilla"
# stock3 = "coffee"
# stock4 = "green tea"

# # Expected Output
# # Yes, we have vanilla in stock
# flav_order = input("Please enter your favorite flavor 🍧:").lower()

# if flav_order == stock1:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock2:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock3:
#     print(f"Yes, we have {flav_order} in stock!")
# elif flav_order == stock4:
#     print(f"Yes, we have {flav_order} in stock!")
# else:
#     print(f"Sorry, we ran out of {fav_flavour}...")

# # Sorry, we ran out strawberry
