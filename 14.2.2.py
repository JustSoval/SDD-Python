# Created by Jesse Williamson, 25th February 2021
# Gets integer input from user and checks whether it is divisible by 7

def inputData():
    while True:
        try:
            numInput = int(input("Please enter an integer value >>>> "))
            return numInput
        except:
            print("Invalid value!")

def processData(numInput):
    if numInput % 7 == 0:
        return "This number is divisible by 7!"
    else:
        return "this number is not divisible by 7!"

print(processData(inputData()))