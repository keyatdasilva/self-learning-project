name = input("What is your name? ")
city = input("What city do you stay in? ")
print("Hi", name,", I hear", city, "is a great place!")

length = int(input("What's the length of the room? In metres "))
width = int(input("What's the width of the room? In metres "))
area_of_room = length * width 
print("The total area of the room is", area_of_room)

price = float(input("What is the price? In Rands "))
discount = float(price * 0.85)
print("The discounted price is R", round(discount, 2))