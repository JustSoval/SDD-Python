# Created by Jesse Williamson, 15th February 2021
# Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.



#### ATTEMPT 1 ####
# This did not work because the while loop condition can not be checked while shopping_list is empty.

# shopping_list = []

# print("This program will allow you to enter items to a shopping list. Enter an empty string to terminate the program.")
# while shopping_list[-1] != "":
#  item = input("Enter an item or empty string: ")
#  shopping_list.append(item)

# print(shopping_list)



#### Attempt 2 ####
# Sucessful

shopping_list = []

print("\nThis program will allow you to enter items to a shopping list. Enter an empty string to terminate the program.")
# loop until break
while True:
    # Get user input and add to list
    item = input("Enter an item or empty string >>>> ")
    shopping_list.append(item)

    # check if last item is empty
    if shopping_list[-1] == "":
        # Break loop and print list
        break

# print every item in shopping list in a dot point list (-1 to remove the empty string)
print("\nList items:")
for i in (shopping_list[:-1]):
    print("-" + i)
print()