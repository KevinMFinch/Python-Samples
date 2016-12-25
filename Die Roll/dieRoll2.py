import random

def rollSix():
	num = random.randint(1,6)
	return num

def rollTwelve():
	num = random.randint(1,12)
	return num

def rollTwoSixes():
	return rollSix() + rollSix()

file = open("diceRolls.csv","w")

for x in range(1000):
	twoSixes = rollTwoSixes()
	twelve = rollTwelve()
	file.write(str(twoSixes)+", "+str(twelve)+"\n")

file.close()