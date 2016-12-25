numRows = int(input("How many rows? "))
for y in range(numRows):
    if(y == 0 or y == numRows-1):
        for x in range(numRows*2):
            print("o",end="")
        print()
    else:
        print("o",end="")
        for x in range((numRows*2) - 2):
            print(" ",end="")
        print("o",end="")
        print()
        
            
