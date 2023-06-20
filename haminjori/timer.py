import time
from os import system,name
while True:
    choice = input("Do ypu want to Start?(y/n)")
    if 'y' in choice.lower():
        hour = int(input("Enter Amount of hour:"))
        minutes = int(input("Enter Amount of minutes:"))
        seconds = int(input("Enter Amount of seconds:"))
        total = hour * 3600 + minutes * 60 + seconds
        time.sleep(1)
        while total >=1:
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
        print("time ended")

    elif 'n' in choice.lower():
        print("Exiting....")
        break
    else:
        print("Invalid input")