import random

print("Hello! Welcome to HorseGame by Kevin Finch.")
print("You have stolen a horse from the queen and you need to cross the Pelennor Fields to reach safety.")
print("The queen's soldiers are chasing you to get the horse back!")
print("Survive your 200 mile journey and outrun the soldiers.")

options = ["A. Drink from your canteen.","B. Ahead moderate speed.","C. Ahead full speed.","D. Stop for the night.","E. Status check.","F. Quit."]
gameOver = False
wonGame = False

waterLeft = 6
thirst = 0
milesTravelled = 0
enemyDistance = -20
horseFatigue = 0

while(gameOver == False):
	for x in range(len(options)):
		print(options[x])
	choice = raw_input().upper()

	if(choice == "F"):
		gameOver = True
	elif(choice == "E"):
		print("Miles Travelled: "+str(milesTravelled))
		print("Drinks in canteen: "+str(waterLeft))
		milesBack = milesTravelled - enemyDistance
		print("The natives are "+str(milesBack)+" miles behind you.")
	elif(choice == "D"):
		horseFatigue = 0
		enemyDistance += random.randint(7,14)
		print("Your horse is now rested.")
	elif(choice == "C"):
		temp = random.randint(10,20)
		milesTravelled += temp
		print("You travelled "+str(temp)+" miles.")
		thirst += 1
		enemyDistance += random.randint(7,14)
		horseFatigue += random.randint(1,3)
	elif(choice == "B"):
		temp = random.randint(5,12)
		milesTravelled += temp
		print("You travelled "+str(temp)+" miles.")
		thirst += 1
		enemyDistance += random.randint(7,14)
		horseFatigue += 1
	elif(choice == "A"):
		if(waterLeft > 0):
			waterLeft -= 1
			thirst = 0 
		else:
			print("You don't have water to drink!")

	if(random.randint(1,20) == 1):
		print("You found a well! You now have water, and are well rested.")
		waterLeft = 6
		thirst = 0
		horseFatigue = 0

	if(thirst > 6):
		print("You died of thirst.")
		gameOver = True 
	elif(thirst > 4):
		print("You are thirsty.")

	if(gameOver == False):
		if(horseFatigue > 8):
			print("Your horse died.")
			gameOver = True
		elif(horseFatigue >5):
			print("Your horse is tired.")

	if((milesTravelled - enemyDistance) <= 0):
		print("The soldiers caught you. You lose.")
		gameOver = True
	elif((milesTravelled-enemyDistance) <= 15):
		print("The soldiers are getting close!")

	if(gameOver == False):
		if(milesTravelled >= 200):
			print("You escaped! Well done.")
			gameOver = True