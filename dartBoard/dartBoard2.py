import random
import math

def throwDart():
	xPos = random.randint(-100,100)
	yPos = random.randint(-100,100)
	return math.sqrt( pow(xPos,2) + pow(yPos,2) )

numTimes = [10,100,500,1000,5000,10000,50000]

file = open("Darts.csv","w")

for x in range(len(numTimes)):
	arr = [0,0,0,0]
	for y in range(numTimes[x]):
		radius = throwDart()
		if(radius < 25):
			arr[0] += 1
		elif(radius < 50):
			arr[1] += 1
		elif(radius < 100):
			arr[2] += 1
		else:
			arr[3] += 1
	file.write(str(numTimes[x])+","+str(arr[3])+","+str(arr[2])+","+str(arr[1])+","+str(arr[0])+"\n")

file.close()