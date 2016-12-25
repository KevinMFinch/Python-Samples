score = 0 
questions = ["How many roads must a man walk down? ","Is Tejas good looking? (Yes/No) ","How many quarters make a dollar? ","Who is the coolest of these people:\nKevin\nTejas\nVedanta\n","How many letters are in the alphabet? "]
answers = ["42","NO","4","KEVIN","26"]

for x in range(len(questions)):
	response = raw_input(questions[x])
	if(response.upper() == answers[x]):
		score+=1
		print("You got it right!")
	else:
		print("Incorrect.")

percentage = (score + 0.0)/len(questions) * 100

print("You answered "+str(score)+" out of "+str(len(questions))+" right.")
print("That is a score of "+str(percentage)+" percent.")