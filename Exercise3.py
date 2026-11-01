# Question1
# if x = 20 and y = 4
# Subtract 5 from x using the -= operator
# Multiply y by 3 using the *= operator
# Divide x by y and store the result in a variable called result
# Print result with a label

x = 20 
y = 4 

x -= 5
y *= 3 
result = x/y 
print("This is the result", result)

# Question 2
# if a = 8, b = 12 and c = 5
# Create a condition that checks if b is greater than a
# Create a condition that checks if a is even
# Create a condition that checks if c is greater than or equal to a
# Combine them into a variable called final_condition. It should be True if either:
# b is greater than a, or
# a is even and c is greater than or equal to a
# Print final_condition with a label

a = 8 
b = 12
c = 5

b_greater_than_a = b>a 
a_even = a % 2 
c_greater_than_or_equal_to_a = c>=a 
final_condition = b_greater_than_a or (a_even and c_greater_than_or_equal_to_a)
print("The result is",final_condition)

# Question 3 
# Ask the user for the temperature in °C and store it as an integer in a variable called temp
# Use if, elif and else to print a message:
# 30 or above: Hot
# 20 to 29: Warm
# 10 to 19: Cool
# Below 10: Cold

temp = int(input("What's the temperature? In Celcius "))
if temp >= 30:
    print("Hot")
elif temp >= 20:
    print("Warm")
elif temp >= 10:
    print("Cool")
else:
    print("Cold")

# Question 4
# Ask the user for two numbers and store them in num1 and num2 (use float)
# Ask the user for an operation (+, -, *, /) and store it in operation
# Use if / elif / else to do the chosen operation
# If they choose / and num2 is 0, print a message like You can't divide by zero! instead of crashing
# Print the result with a label

num1 = float(input("Value? "))
num2 = float(input("Value? "))
operation = input("Which operation would you like to use? +,-,*,/: ")
if operation == "+": 
    print("Result", num1 + num2)
elif operation == "-": 
    print("Result ", num1 - num2)
elif operation == "*":
    print("Result ", num1 * num2)
elif operation == "/":
    if num2 == 0:
        print("You can't divide by 0")
    else: 
        print("Result ", num1 / num2)
else: 
    print("Sorry, that's not a valid operation.")


# New Exercise based on the same fundamentals

# Question 1 
# x = 50 and y = 5
# Add 10 to x using the += operator
# Divide y by 5... actually, multiply y by 4 using the *= operator
# Divide x by y and store the result in a variable called result
# Print result with a label

x = 50 
y = 5 

y *= 4
result = x/y 
print ("The result is ",result)

# question 2
# a = 15
# b = 6
# c = 20
# Create a condition that checks if a is greater than c
# Create a condition that checks if b is even
# Create a condition that checks if c is greater than or equal to a
# Combine them into a variable called final_condition. It should be True if either:
# a is greater than c, or
# b is even and c is greater than or equal to a
# Print final_condition with a label

a = 15
b = 6
c = 20 

a_is_greater_than_c = a>c 
b_is_even = b % 2 
c_greater_than_or_equal_a = c>=a 
final_condition = a_is_greater_than_c or (b_is_even and c_greater_than_or_equal_a)
print("The result is ", final_condition)

# question3
# Ask the user for their age and store it as an integer in a variable called age
# Use if, elif and else to print a message:
# 65 or above: Senior
# 18 to 64: Adult
# 13 to 17: Teenager
# Below 13: Child

age = int(input("What is your age? "))
if age >= 65: 
    print("Senior")
elif age >= 18: 
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Question4 
# Ask the user for a price and store it as a float in price
# Ask the user for a discount code and store it in code
# Use if / elif / else to work out the new price:
# SAVE10: 10% off (price * 0.90)
# SAVE20: 20% off (price * 0.80)
# FREE: the price becomes 0
# Anything else: print a message saying the code isn’t valid

price = float(input("What is the price? In Rands ")) 
code = input("Do you have a discount code? ")
if code == "SAVE10":
    print("The cost will be R",price * 0.90)
elif code == "SAVE20":
    print("The cost will be R",price * 0.80)
elif code == "FREE":
    print("The item is free")
else:
    print ("Your code isn't valid")