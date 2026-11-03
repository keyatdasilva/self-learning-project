
# Question 1 
# p = 4
# q = 6
# r = 9
# Add 2 to p using +=
# Multiply q by 3 using *=
# Modulo r by 5 using %=
# Calculate the square root of (p² + q² + r²) and save it in distance
# Print distance rounded to 2 decimal places, with a label

import math 
# p = 4
# q = 6
# r = 9

# p+=2 
# q*=3
# r%=5

# distance = math.sqrt(p**2 + q**2 + r**2)
# print("The distance is",round(distance, 2))

# Question2
# Ask the user for three integers: x, y, z
# Create three conditions, each saved in its own variable:
# is_odd: True if x is odd
# is_negative: True if y is less than 0
# is_in_range: True if z is between 20 and 80
# Create final_condition, which is True only if all three are True
# Print final_condition with a label

# x = int(input("Enter the first number (x): "))
# y = int(input("Enter the second number (y): "))
# z = int (input("Enter the third number (z): "))

# is_odd = x % 2 == 1 
# is_negative = y < 0 
# is_in_range = z >= 20 and z <= 80 
# final_condition = is_odd and is_negative and is_in_range
# print("The condition is",final_condition)


# Question3 
# Ask the user for their base score (an integer)
# Add 8 bonus points, then subtract a late penalty of 15
# Keep the score between 0 and 100 using min() and max()
# Use if / elif / else to print the grade:
#75 or above: Distinction 
# 50 to 74: Pass
# Below 50: Fail
# Print the final score with a label too

# score = int(input("Enter your score: "))
# score += 8 
# score -= 15
# score = min(score, 0)
# score = max(score, 100)

# print("Your final score is",score)

# if score >=75:
#   print("Distinction")
# elif score >=50:
#   print("Pass")
# else:  
#   print("Fail")



# Question4 
# Ask the user for two numbers (use float) and an operation (+, -, *, /, %, **)
# Use if / elif / else to do the chosen operation
# For / and %, use try / except to catch division by zero
# If the operation isn’t one of those six, print a message saying it’s not valid
# Print the result with a label

# num1 = float(input("Enter your first number: "))
# num2 = float(input("Enter your second number: "))
# operation = input("Choose your operation (+, -, /, %, *,**): ")

# if operation == "+":
  # print("Result:",num1 + num2)
# elif operation == "-":
#   print("Result:",num1-num2)
# elif operation == "*":
#   print("Result:",num1 * num2)
# elif operation == "/":
#   try: 
#     print("Result:",num1 / num2)
#   except ZeroDivisionError:
#     print("You cannot divide by 0")
# elif operation == "%": 
#   try:
#     print("Result:",num1 % num2)
#   except ZeroDivisionError:
#     print("You cannot divide by 0")
# elif operation == "**":
#   print("Result:",num1 ** num2)
# else:
#   print("It's not valid")

# ---------------------------------------------------------------------------------

# Exercise from Claude (Trying it on my own)

# Question 1 

# import math

# m = 10
# n = 3
# k = 14
# Subtract 4 from m using -=
# Multiply n by 5 using *=
# Modulo k by 6 using %=
# Calculate the square root of (m² + n² + k²) and save it in length
# Print length rounded to 2 decimal places, with a label

import math 

m = 10 
n = 3 
k = 14

m -= 4
n *= 5 
k %= 6

length = math.sqrt(m**2 + n**2 + k**2 )
print("The length is", round(length, 2))

# Question2 
# Ask the user for three integers: a, b, c
# Create three conditions, each saved in its own variable:
# is_even: True if a is even
# is_positive: True if b is greater than 0
# is_in_range: True if c is between 5 and 25
# Create final_condition, which is True only if is_even is True and at least one of is_positive or is_in_range is True
# Print final_condition with a label

a = int(input("Enter your first number (a): "))
b = int(input("Enter your second number (b): "))
c = int (input("Enter your third number (c): "))

is_even = a % 2 == 0
is_positive = b > 0 
is_in_range = c >= 5 and c <= 25 
final_condition = is_even and (is_positive or is_in_range)
print ("The condition is:", final_condition)

# Question 3 
# Ask the user for their base mark (an integer)
# Add 10 bonus points, then subtract a penalty of 20
# Keep the mark between 0 and 100 using min() and max()
# Print the final mark with a label
# Use if / elif / else to print the result:
# 80 or above: Excellent
# 50 to 79: Good
# Below 50: Needs work
    
score = int(input("Please enter your base mark: "))
score += 10 
score -= 20
score = max(score, 0)
score = min(score, 100)
print("Final score:",score)

if score >=80:
  print("Excellent")
elif score >=50:
  print("Good")
else: 
  print("Needs work")

# Question 4 
# Ask the user for two numbers (use float) and an operation (+, -, *, /, //, **)
# Use if / elif / else to do the chosen operation
# For / and //, use try / except to catch division by zero
# If the operation isn’t one of those six, print a message saying it’s not valid
# Print the result with a label

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operation = input("Enter your operation(+, -, *, /, //, **): ")

if operation == "+":
  print("Result:",num1 + num2)
elif operation == "-":
  print("Result:",num1 - num2)
elif operation == "*":
  print("Result:",num1 * num2)
elif operation == "/":
  try: 
    print("Result:",num1 / num2)
  except ZeroDivisionError:
    print("You cannot divide by zero!")
elif operation == "//":
  try: 
    print("Result:",num1//num2)
  except ZeroDivisionError:
    print("You cannot divide by zero!")
elif operation == "**":
  print("Result:",num1**num2)
else:
  print("Invalid operation")






