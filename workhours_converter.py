# Work-time converter for Chrystal
# It will ask the input from her about how many hours & minutes she has worked
# for the day and how much she has left for the day & week.
import time
def main():
    dayOrWeek = input("Checking amt. of time left for today or for the week? \nEnter d for day, w for week.\n")
    if dayOrWeek == 'd':
        amountWorked_Day = float(input("Enter the amount of hours you have worked for the day, including the decimals: \n"))
        hoursLeft_Day =  8 - amountWorked_Day // 1 # takes only the integer of the input and calculates the hours left in the workday.
        minsLeft_Day = 60 - (amountWorked_Day % 1) * 60 # takes only the decimal #s of the input and calculates the minutes left in the workday.
        if amountWorked_Day.is_integer():
            print("Hours remaining for the day: " + str(int(hoursLeft_Day)) + " hours")
            time.sleep(6)
        else:
            print("Hours & minutes remaining for the day: " + str(int(hoursLeft_Day) - 1) + " hours & " + str(int(minsLeft_Day)) + " minutes")
            time.sleep(6)
    elif dayOrWeek == 'w':
        amountWorked_Week = float(input("Enter the amount of hours you have worked for the week, including the decimals: \n"))
        hoursLeft_Week = 40 - amountWorked_Week // 1 # takes only the integer of the input and calculates the hours left in the workweek.
        minsLeft_Week = 60 - ((amountWorked_Week % 1) * 60) # takes only the decimal #s of the input and calculates the minutes left in the workweek.
        if amountWorked_Week.is_integer():
            print("Hours remaining for the week: " + str(int(hoursLeft_Week)) + " hours")
            time.sleep(6)
        else:
            print("Hours & minutes remaining for the week: " + str(int(hoursLeft_Week) - 1) + " hours & " + str(int(minsLeft_Week)) + " minutes")
            time.sleep(6)
        
main()
