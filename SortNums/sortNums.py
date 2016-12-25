import random

arr = []

def insertionsort():
  for i in range( 1, len( arr ) ):
    tmp = arr[i]
    k = i
    while k > 0 and tmp < arr[k - 1]:
        arr[k] = arr[k - 1]
        k -= 1
    arr[k] = tmp

f= open("RandNum100.txt","w")
for x in range(100):
	f.write(str(random.randint(1,500))+"\n")
f.close()

fileName = "RandNum100.txt"
num_lines = sum(1 for line in open(fileName))

f = open(fileName,"r")

for i in range(num_lines):
	arr.append(int(f.readline()))

f.close()

insertionsort()

file = open("SortNum100.txt","w")

for x in range(len(arr)):
	file.write(str(arr[x])+"\n")

file.close()