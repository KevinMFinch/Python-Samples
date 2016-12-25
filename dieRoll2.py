import random

def main():
    done = False
    while not done:
        menu()
        choice = raw_input("Enter choice:  ")
        if choice.lower() == "a":
            numRolls = raw_input("Enter number of rolls ")
            for i in range(int(numRolls)):
                roll = rollSix()
                print "Roll #",i + 1,":",roll
            
        elif choice.lower() == "b":
            numRolls = raw_input("Enter number of rolls ")
            for i in range(int(numRolls)):
                num = rollTwelve()
                print "Roll #",i + 1,":",num
        elif choice.lower() == "c":
            done = True
        else:
            print "Invalid input"
            
            
                           
def menu():
    print "A.  Roll six sided die"
    print "B.  Roll twelve sided die"
    print "C.  Roll two six sided dice"
    print "D.  Quit"

def rollSix():
    num = random.randint(1,6)
    return num

def rollTwelve():
    num = random.randint(1,12)
    return num

main()