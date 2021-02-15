# Created by Jesse Williamson, 15th February 2021
# Improve 13.2.1 so that you are presented with a menu enabling you to either add items to the list, sort the list, display the list, delete the list or exit the program.

options = {
    1 : add
    2 : sort
    3 : display
    4 : reset
    5 : terminate
}

def add():
    

while True:
    print("\nShopping List.")
    print("This program can add items to a shopping list and also sort and delete the list.")
    print()
    print("1. Add items to the list")
    print("2. Sort the list ")
    print("3. Display the list")
    print("4. Reset the list")
    print("5. Terminate the program")
    # Get user input as an integer
    try:
        selection = int(input("\nPlease select an option >>> "))
    except (ValueError):
        print("\n====== Invalid input, please retry. ========")
        continue



options[selection]()