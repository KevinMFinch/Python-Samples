num = int(input("What is n?"))
maxNum= (2*num)-1
initialList = []
numSpaces = 2
for x in range(0,maxNum,2):
    initialList.append(x+1)
for x in range(maxNum,0,-2):
    initialList.append(x)

for y in range(num):
    for x in range(len(initialList)):
        print(initialList[x],end=" ")
        if(x < len(initialList) -1 and y > 0 and initialList[x] == initialList[x+1]):
            for z in range(numSpaces):
                print(" ",end=" ")
            numSpaces+=2
    print()
    if(num - y > 1):
        initialList.pop(0)
        initialList.pop()

numSpaces-=2
for y in range(num):
    for x in range(len(initialList)):
        print(initialList[x],end=" ")
        if(x < len(initialList) -1 and y < num and initialList[x] == initialList[x+1]):
            for z in range(numSpaces):
                print(" ",end=" ")
            numSpaces-=2
    print()
    last = initialList[-1]
    
    initialList.insert(0,last - 2)
    initialList.append(last - 2)
    
    
