fileName = "DataSorted10000.txt"
num_lines = sum(1 for line in open(fileName))

f = open(fileName,"r")
arr = []

for i in range(num_lines):
	arr.append(int(f.readline()))

f.close()

def linearSearch(value):
	for x in range(len(arr)):
		if(arr[x] == value):
			return ("Found value at position "+str(x))
	return("Not found, checked "+str(len(arr)))

def binarySearch(value):
	first = 0
	count = 0
	last = len(arr)-1
	found = False

	while (first<=last and not found):
		count+=1
		midpoint = (first + last)//2
		if (arr[midpoint] == value):
			found = True
			return("Found at position "+str(midpoint)+" after "+str(count)+" iterations.")
		else:
			if (value < arr[midpoint]):
				last = midpoint-1
			else:
				first = midpoint+1
	return("Did not find after "+str(count)+" iterations.")

print(binarySearch(54798))