import random
import math

def throwDart():
	xPos = random.randint(-100,100)
	yPos = random.randint(-100,100)
	return math.sqrt( pow(xPos,2) + pow(yPos,2) )

numTimes = 0
score = 0
arr = [0,0,0,0]

while(numTimes < 1):
	numString = raw_input("How many times would you like to throw a dart? ")
	if(numString.isdigit() == True):
		numTimes = int(numString)
	if(numTimes < 1):
		print("You did not enter a valid number. Please enter another. ")

for x in range(numTimes):
	radius = throwDart()
	if(radius < 25):
		score += 5
		arr[0] += 1
	elif(radius < 50):
		score += 3
		arr[1] += 1
	elif(radius < 100):
		score += 1
		arr[2] += 1
	else:
		arr[3] += 1


print("You got "+str(arr[0])+" bullseyes, "+str(arr[1])+" middle circle hits, "+str(arr[2])+" outer circle hits, and "+str(arr[3])+" misses.")
print("You scored "+str(score)+" points.")