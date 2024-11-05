# quote = "I love python"
# # [] -> square bracket
# # Numbers inside the [] are "Indexes"
# # print(quote[2])
# # print(quote[3])

# # Want to print "love"
# # print(quote[2] + quote[3] + quote[4] + quote[5])
# # quote[start:end:skip] # end is not included
# print(quote[2:6])
# print(quote[2:])
# print(quote[2:10:2])

# print(quote[-1])
# print(quote[-1:])

# print(quote[::-1]) # flips the message
# print(quote[:-1])


# name = "  Anny"
# print(name.upper())
# print(name.lower())

# print(name.strip())

# Task
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Expected Output
# "PYTHON-POWERFUL"

#Solution 1: 
# store_pythonpowerful = secret_message[18:24] + "-" + secret_message[37:45]
# print(store_pythonpowerful.upper())

#Solution 2 :


# 1. Solve the problem.
# 2. Make it better.

# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"
# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"
# Python with powerful opportunities and Endless fun!
# MY ANSWER
# original_msg = flipped_message[::-1] 
# expected_msg = original_msg[0:6] + " 🗡️ " + original_msg[11:20] + " 🌸"
# print(expected_msg.lower())

# Teacher's Solution
original_msg = flipped_message[::-1] 
print(f"{original_msg[0:6]} 🗡️ {original_msg[11:20]} 🌸".lower())