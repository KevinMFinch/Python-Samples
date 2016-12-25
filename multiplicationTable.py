for i in range(1,11):
    for j in range(1,11):
        product = i*j
        endOfLine = ""
        if(product > 9 and product < 100):
            endOfLine = " "
        elif(product < 10):
            endOfLine = "  "
        print(product, end= endOfLine)
    print()
