
import random

file = open("answers.txt","w")

def intInput(query):
    while True:
        try:
            return int(input(query))
        except:
            print("Invalid value!")

selection = 12
row = list(range(1,12+1))
random.shuffle(row)



def getTableNumber():
    selection = intInput("Please enter an integer to be processed")
    return selection

row = list(range(1,selection+1))
random.shuffle(row)

def process(selection, row):
    question = "\nWhat is {} x {}? >>>> ".format(selection, row[i])
    answer = selection*row[i]
    guess = int(intInput(question))
    if guess == (answer):
        print("Correct")
        file.write(question+str(guess)+" ✓")
    else:
        print("Incorrect!")
        print("The answer was {}.".format(answer))
        file.write(question+str(guess)+" 🗙    "+"("+str(answer)+")")


for i in row:
    print(i)
    process()


# file.close()