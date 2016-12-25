numList = []
while(len(numList) < 10):
    numList.append(int(input("Enter a number please ")))

print("Even sum: ",end="")
evenSum =0
for i in range(len(numList)):
    if(numList[i] % 2 == 0):
        evenSum += numList[i]
print(evenSum)

print("Odd sum: ",end="")
oddSum =0
for i in range(len(numList)):
    if(numList[i] % 2 == 1):
        oddSum += numList[i]
print(oddSum)
