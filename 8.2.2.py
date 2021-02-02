# Using a for loop to allow the user to input 6 items for a shopping list from the keyboard and print the list on screen.
# - Jesse Williamson, 2 Feb 2021

# shopping_list = []
# for i in range(6):
#     shopping_list.append(input("What would you like to add the the shopping list? >>>> "))

# print(shopping_list)

backpack = {}

backpack['monday'] = []
backpack['tuesday'] = []
backpack['wednesday'] = []
backpack['thursday'] = []
backpack['friday'] = []

print(backpack['monday'])

while True:
    print("Please select one of the following options: \n")
    print("1. A day - input a day, e.g. 'Monday' to acess the items for that day.")
    print("2. An output of your required items for the week - input 'output' for this option")
    print("3. Exit - input 'exit' to exit the program.\n")
    selection = input("Select >>> ").lower()

    if selection == "monday":
        if backpack['monday']: 
            print("\nThe current items for Monday are: \n")
        for i in backpack['monday']:
            print(i+',')
        backpack['monday'].append(input("\nWhat would you like to add? >>> "))
        print("Your item has been added!")

    elif selection == "tuesday":
        if backpack['tuesday']: 
            print("\nThe current items for Tuesday are: \n")
        for i in backpack['tuesday']:
            print(i+',')
        backpack['tuesday'].append(input("\nWhat would you like to add? >>> "))
        print("Your item has been added!")

    elif selection == "wednesday":
        if backpack['wednesday']: 
            print("\nThe current items for Wednesday are: \n")
        for i in backpack['wednesday']:
            print(i+',')
        backpack['wednesday'].append(input("\nWhat would you like to add? >>> "))
        print("Your item has been added!")

    elif selection == "thursday":
        if backpack['thursday']: 
            print("\nThe current items for Thursday are: \n")
        for i in backpack['thursday']:
            print(i+',')
        backpack['thursday'].append(input("\nWhat would you like to add? >>> "))
        print("Your item has been added!")

    elif selection == "friday":
        if backpack['friday']: 
            print("\nThe current items for Friday are: \n")
        for i in backpack['friday']:
            print(i+',')
        backpack['friday'].append(input("\nWhat would you like to add? >>> "))
        print("Your item has been added!")

    elif selection == "output":
        print("\n"+backpack+"\n")



print 