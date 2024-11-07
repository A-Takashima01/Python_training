# Range always starts with 0
# for i in range(3):
#     print(i)

# range -> simular to slice

# range (start, end) # end is included
# for i in range(1, 4):
#     print(i)

# Task - Convert below to for loop

# i = 1

# while i <= 5:
#     print("🔥" * i)
#     i = i + 1
# Task 1.1 - Convert below to for loop

# i = 1

# for i in range(1, 6):
#     print("🔥" * i)
#     i = i + 1

# Task 1.2 - Convert below to for loop

# i = 1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# while i <= rows:
#     print(pattern * i)
#     i = i + 1

# rows = int(input("Please tell me the no of rows. "))
# pattern = input("Please tell the pattern?: ")
# for i in range(1, rows + 1, 2):
#     print(pattern * i)

# Select, ctrl + D -> multi cursor


# Task
# Geometric progression
# 4
# 16
# 36
# 64
# 100
# 144

for i in range(2, 13, 2):
    print(i, i**2)
