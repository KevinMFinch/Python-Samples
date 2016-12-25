import random

tailCount = 0
headCount = 0
for x in range(1000000):
	coin = random.randint(0,1)

	if(coin == 0):
		headCount+=1
	else:
		tailCount+=1

print("You got "+str(tailCount)+" tails and "+str(headCount)+" heads.")