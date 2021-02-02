# Using a for loop to allow the user to input 6 items for a shopping list from the keyboard and print the list on screen.
# - Jesse Williamson, 2 Feb 2021

shopping_list = []
for i in range(6):
    shopping_list.append(input("What would you like to add the the shopping list? >>>> "))

print(shopping_list)