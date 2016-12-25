numList = [10,18,4,8,20,3]
sum = 0
for item in numList:
	sum+=item
print("Sum: "+str(sum))
smallest = numList[0]
for item in numList:
	if(item < smallest):
		smallest = item
print("Smallest:" +str(smallest))

for i in range(5):
	for x in range(i+1):
		print("*", end="")
	print()
