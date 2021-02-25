# Created by Jesse Williamson, 15th February 2021
# Improve 13.2.1 so that you are presented with a menu enabling you to either add items to the list, sort the list, display the list, delete the list or exit the program.

shopping_list = []

def add():
    shopping_list.append(input("\nWhat would you like to add? >>>> "))
    
def sort():
    return "oof"

def display():
    print("\nList items:")
    for i in (shopping_list[:-1]):
        print("-" + i)
    print()

def reset():
    shopping_list = []

def terminate():
    raise SystemExit


options = {
    1 : add,
    2 : sort,
    3 : display,
    4 : reset,
    5 : terminate
}



    

while True:
    print("\n===========================================================")
    print("\nShopping List.")
    print("This program can add items to a shopping list and also sort and delete the list.")
    print()
    print("1. Add items to the list")
    print("2. Sort the list ")
    print("3. Display the list")
    print("4. Reset the list")
    print("5. Terminate the program")
    # Get user input as an integer
    



    # try:
    #     selection = int(input("\nPlease select an option >>> "))
    #     print("\n===========================================================")
    # except (ValueError):
    #     print("\n====== Invalid input, please retry. ========")
    #     continue

    # if options[selection] in globals():
    #     continue
    # else:
    #     print("\n===========================================================")
    #     print("Selection does not exist!")
    #     continue

    try:
        selection = int(input("\nPlease select an option >>> "))
        options[selection]()
    except:
        print("\n=============== Invalid input, please retry. ===============")
        