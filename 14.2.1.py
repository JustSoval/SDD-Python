# Created by Jesse Williamson, 25th February 2021
# Gets integer input from user and returns it 

def inputData():
    while True:
        try:
            numInput = int(input("Please enter an integer value >>>> "))
            return numInput
        except:
            print("Invalid value!")

print(inputData())