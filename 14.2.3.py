# Created by Jesse Williamson, 25th February 2021
# Gets integer input from user, checks whether it is divisible by 7, and returns it

def inputData():
    while True:
        try:
            numInput = int(input("Please enter an integer value >>>> "))
            return numInput
        except:
            print("Invalid value!")

def processData(numInput):
    if numInput % 7 == 0:
        numProcessed = "this number is divisible by 7."
    else:
        numProcessed = "this number is not divisible by 7."
    return numInput, numProcessed

def outputData(numInput, numProcessed):
    print("You entered the number {}, {}".format(numInput, numProcessed))

num, answer = processData(inputData())
outputData(num, answer)