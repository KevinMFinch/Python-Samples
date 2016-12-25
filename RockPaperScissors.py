import random

gameOver = False

while(gameOver == False):
	userChoice = ""
	inputValid = False

	while(inputValid == False):
		userChoice = raw_input("What do you throw? (rock/paper/scissors) ")
		userInt = 0
		if(userChoice.upper() == "ROCK"):
			userInt = 0 
			inputValid = True
		elif(userChoice.upper() == "PAPER"):
			userInt = 1
			inputValid = True
		elif(userChoice.upper() == "SCISSORS"):
			userInt = 2
			inputValid = True
		else:
			print("Enter a valid throw please.")

	compChoice = random.randint(0,2)
	throws = ["rock","paper","scissors"]

	print("You threw "+userChoice.lower())
	print("The computer threw a "+throws[compChoice])

	if(userInt == compChoice +1):
		print("You win!")
	elif(userInt ==0 and compChoice == 2):
		print("You win!")
	elif(userInt == compChoice):
		print("You tied!")
	else:
		print("You lost!")

	print("Do you want to play again? (y/n) ")
	if(raw_input().upper() == "N"):
		gameOver = True