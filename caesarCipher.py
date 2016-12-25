def encryptString(st):
	newStr = ""
	for x in range(len(st)):
		asciiNum = ord(st[x])
		shiftedNum = asciiNum + key
		if(shiftedNum > 122):
			shiftedNum -= 26
		if(st[x] != " "):
			newStr += chr(shiftedNum)
		else:
			newStr += " "
	print("The shifted string is: "+newStr)

def decryptString(st):
	newStr = ""
	for x in range(len(st)):
		asciiNum = ord(st[x])
		shiftedNum = asciiNum - key
		if(shiftedNum < 97):
			shiftedNum += 26
		if(st[x] != " "):
			newStr += chr(shiftedNum)
		else:
			newStr += " "
	print("The shifted string is: "+newStr)	

gameOver = False
while(gameOver == False):
	print("Hello! Welcome to the Casesar Cipher Program! Please pick an option below.")
	print("a. encode")
	print("b. decode")
	print("c. quit")

	choice = raw_input("Enter a choice: ")
	while(choice.lower() != "a" and choice.lower() != "b" and choice.lower() != "c"):
		choice = raw_input("Invalid choice. Please choose another. ")
	if(choice.lower() == "c"):
		quit()
	string = raw_input("Please enter a string to encrypt or decrypt. ").lower()
	key = int(raw_input("How many letter should the shift be? "))
	print("That will shift the string by: "+str(key))
	if(choice.lower() == "a"):
		encryptString(string)
	elif(choice.lower() == "b"):
		decryptString(string)

	if(raw_input("Do you want to enter another string? (Y/N) " ).lower() == "n"):
		gameOver = True
		quit()