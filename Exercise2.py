# Question 1
# Ask the user for their favourite subject and save it in a variable
# Ask the user for their favourite sport and save it in a variable
# Print a sentence using both, like: I love Maths, but I also enjoy playing Soccer!

favourite_subject = input("What is your favourite subject? ")
favourite_sport = input("What is your favourite sport? ")
print("I love",favourite_subject,", but I also enjoy playing",favourite_sport)

# Question2
# Ask the user for the number of people coming to a party, stored as an integer
# Ask the user for the number of slices of pizza each person will eat, stored as an integer
# Calculate the total slices needed
# Print the result with a label

amount_of_people = int(input("How many people will attend the party? "))
number_of_slices = int(input("How many slices will each person get? "))
total_slices_needed = amount_of_people * number_of_slices 
print("You will need", total_slices_needed,"slices of pizza.")

# Question3
# Ask the user for a bill amount in rand, stored as a float
# Calculate a 10% tip using the formula: bill * 0.10
# Print the tip rounded to 2 decimal places

bill = float(input("What is the bill? In Rands "))
tip = float(bill * 0.10)
print("The amount of the tip will be R", round(tip, 2))