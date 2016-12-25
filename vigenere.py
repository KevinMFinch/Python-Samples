matrix = []
for x in range(26):
	matrix.append([])

def encryptString(string,key):
	lenKey = len(key)
	string = string.upper()
	newStr = ""
	indexForCipher = 0
	row = 0
	for x in range(len(string)):
		if(string[x] != " "): 
			firstLetter = key[indexForCipher % lenKey]
			row = ord(firstLetter)-65
			newStr += matrix[row][ord(string[x]) - 65]
			indexForCipher+=1
		elif(string[x] == " "):
			newStr+=" "

	print(newStr)

def decryptString(string, key):
	lenKey = len(key)
	string = string.upper()
	newStr = ""
	indexForCipher = 0
	row = 0
	for x in range(len(string)):
		if(string[x] != " "): 
			firstLetter = key[indexForCipher % lenKey]
			row = ord(firstLetter)-65
			col = matrix[row].index(string[x])
			newStr += matrix[0][col]
			indexForCipher+=1

	print(newStr)

def createMatrix():
	for row in range(0,26):
		for col in range(row,row+26):
			asciiRow = row + 65
			asciiCol = col + 65
			if(asciiCol > 90):
				matrix[row].append(chr(asciiCol-26))
			else:
				matrix[row].append(chr(asciiCol))
	
createMatrix()
print("a. encode")
print("b. decode")
print("c. quit")

choice = input("Enter a choice: ")
while(choice.lower() != "a" and choice.lower() != "b" and choice.lower() != "c"):
	choice = input("Invalid choice. Please choose another. ")
if(choice.lower() == "c"):
	quit()
string = input("Please enter a string to encrypt or decrypt. ").upper()
key = input("What is the keyword to shift by? ").upper()

if(choice.lower() == "a"):
	encryptString(string,key)
elif(choice.lower() == "b"):
	decryptString(string,key)