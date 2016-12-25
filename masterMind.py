import random
import re

userGuess = ""
numGuesses = 0
validLetters = ["a","b","c","d","e","f"]
codeArray = []
gotAnswer = False


def isOnlyLetters(str):
	match = re.search("([A-F]){4}",str)
	return match

def isValidGuess(str):
	if(not (len(str) == 4 and isOnlyLetters(str) and lettersUnique(str))):
		print("Invalid guess. Enter another.")
		return False
	else:
		return True

def lettersUnique(str):
	charArray = []
	allUnique = True

	for i in range(len(str)):
		charArray.append(str[i])

	for i in range(len(charArray)):
		char = charArray.pop(0)
		for x in range(len(charArray)):
			if(char == charArray[x]):
				allUnique = False

	return allUnique

for i in range(4):
	codeArray.append(validLetters.pop(random.randint(0,len(validLetters)-1)).upper())

print(codeArray)
while(numGuesses < 10 and gotAnswer == False):
	while(True):
		userGuess = raw_input("Guess a string of 4 letters between a and f, with no repeats.")
		userGuess = userGuess.upper()
		if(isValidGuess(userGuess) == True):
			break
	print("Guess "+str(numGuesses+1)+": "+userGuess)
	guessArray = []
	for i in range(len(userGuess)):
		guessArray.append(userGuess[i])
	partialMatches = 0
	exactMatches = 0
	for item in guessArray:
		if(item in codeArray):
			if(guessArray.index(item) == codeArray.index(item)):
				exactMatches += 1
			else:
				partialMatches += 1
	if(exactMatches == 4):
		print("You got it!")
		gotAnswer = True
	else:
		print("You have "+str(partialMatches)+" partial matches and "+str(exactMatches)+" exact matches.")
	numGuesses+=1

if(gotAnswer == False):
	print("You did not get the code.")