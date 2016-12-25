daysOfWeek = ["Sunday", "Monday", "Tuesday",
              "Wednesday", "Thursday", "Friday", "Saturday"]
def giveDayOfWeek(dayNum):
    print("The day of the week is: " + daysOfWeek[dayNum])

dayNumber = input("Give a day number to find out what day of the week it is. ")
giveDayOfWeek(int(dayNumber))
