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

# Teacher's Solution
user_1 = input("User 1, please enter your name: ")
user_2 = input("User 2, please enter your name: ")

height_1 = float(input(f"{user_1}, please enter your height: "))
height_2 = float(input(f"{user_2}, please enter your height: "))
# Use absolutes
diff_height = abs(height_1 - height_2)

if height_1 > height_2:
    print(f"{user_1} is taller than {user_2} by {diff_height}cms.")
elif height_1 == height_2:
    print(f"Both {user_1} and {user_2} have the same height.")
else:
    print(f"{user_2} is taller than {user_1} by {diff_height}cms.")
    

# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm

