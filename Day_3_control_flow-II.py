# Loops
# Repeating statemnets
# print("Anny")
# print("Anny")
# print("Anny")

# i = 1

# while i <= 3:
#     print("Anny")
#     i = i + 1

# # Task
# # 🔥
# # 🔥🔥
# # 🔥🔥🔥
# # 🔥🔥🔥🔥
# # 🔥🔥🔥🔥🔥

# i = 1
# while i <= 5:
#     print("🔥" * i)
#     i = i + 1

# # Task 1.2
# # Get number or rows from user
# fire_rows = int(input("How many rows of fire would you like?"))
# i = 1
# while i <= fire_rows:
#     print("🔥" * i)
#     i = i + 1

# Task 1.3
# Pyramid
rows = int(input("Please enter the number of rows: "))
pattern = input("Pattern: ")
i = 1
while i <= rows:
    odd_num = 2 * i - 1
    space = rows - i
    print(" " * (space) + pattern * (odd_num))
    i = i + 1
