import random

def rollSix():
	num = random.randint(1,6)
	return num

def rollTwelve():
	num = random.randint(1,12)
	return num

choice =""
numTimes = 0

while(choice != "C"):
	print("Choose what you want to do.")
	print("a. Roll six sided die.")
	print("b. Roll twelve sided die.")
	print("c. Quit.")
	choice = raw_input("Enter letter of choice: ").upper()
	if(choice == "C"):
		quit()
	else:
		while(numTimes < 1):
			numString = raw_input("How many rolls? ")
			if(numString.isdigit() == True):
				numTimes = int(numString)
			if(numTimes < 1):
				print("You did not enter a valid number. Please enter another. ")

	if(choice == "A"):
		for x in range(numTimes):
			print("Roll #"+str(x+1)+": "+str(rollSix()))
	elif(choice == "B"):
		for x in range(numTimes):
			print("Roll #"+str(x+1)+": "+str(rollTwelve()))
	else:
		print("Please enter a valid letter.")