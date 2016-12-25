import random

randNum = random.randint(1,100)
stillGoing = True
userGuess = 0 
numGuesses = 0 
gotIt = False

print("Guess a number between 1 and 100. You have seven tries.")
while (numGuesses < 7 and stillGoing == True):
	print("Guess "+str(numGuesses+1))
	userGuess = int(raw_input())
	if(userGuess == randNum):
		print("Congrats! You got it!")
		stillGoing = False
	elif(userGuess < randNum):
		print("Too low")
		numGuesses+=1 
	elif(userGuess > randNum):
		print("Too high")
		numGuesses+=1

if(gotIt == False):
	print("Sorry, you failed. The number was "+ str(randNum))