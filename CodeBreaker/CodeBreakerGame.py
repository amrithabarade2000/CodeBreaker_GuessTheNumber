import random

def get_digit():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return (digits[:3])

def get_input():
    guess = list(input("What is your guess? "))
    return guess

def get_clues(secretcode,userinput):

    if userinput == secretcode:
        return "CODE CRACKED"

    clues = []

    for ind,num in enumerate(userinput):
        if num == secretcode[ind]:
            clues.append("Match")
        elif num in secretcode:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues



print("Welcome to Code Breaker!")

secretcode = get_digit()

cluereport = []

while cluereport != "CODE CRACKED":

    userinput = get_input()


    cluereport = get_clues(secretcode,userinput)
    for clue in cluereport:
        print(clue)
