from fullcut import main, clrscr, add_time
from halfcut import main1,add_time1
import time

def divider():
    print("")
    print("+".join(["+"] * 45))
    print("")

def menu_title():
    print("\t\t\t███    ███ ███████ ███    ██ ██    ██\n\t\t\t████  ████ ██      ████   ██ ██    ██ \n\t\t\t██ ████ ██ █████   ██ ██  ██ ██    ██\n\t\t\t██  ██  ██ ██      ██  ██ ██ ██    ██\n\t\t\t██      ██ ███████ ██   ████  ██████ ")

while (True):
    clrscr()
    divider()
    menu_title()
    divider()
    print("\t\t[1] Fullcut (7.15hrs)\t[2] Halfcut (2.5hrs)\t[3] Exit")
    divider()

    menu_choice = input("Enter a number : ")

    divider()

    if menu_choice == "1":
        clrscr()
        divider()
        print("\t\tTree timer scheduler 7.15hrs interval selected")
        divider()
        main()
        print("")

        again = input("Back to main menu? [1] Yes [2] Exit : ")

        if again == "1":
            continue
            time.sleep(2)

        elif again == "2":
            divider()
            print("Exiting the program...")
            divider()

            time.sleep(2)
            break

        else:
            divider()
            print("Invalid input...\tExiting the program...")
            divider()
            time.sleep(2)
            break

    elif menu_choice == "2":
        clrscr()
        divider()
        print("\t\tTree timer scheduler 2.5hrs interval selected")
        divider()
        main1()
        print("")
        again = input("Back to main menu? [1] Yes [2] Exit : ")

        if again == "1":
            continue
            time.sleep(2)

        elif again == "2":
            divider()
            print("Exiting the program...")
            divider()

            time.sleep(2)
            break

        else:
            divider()
            print("Invalid input...\tExiting the program...")
            divider()
            time.sleep(2)
            break

    elif menu_choice == "3":
        print("Exiting Program...")
        divider()
        time.sleep(1)
        break

    else:
        print("Please enter a valid number...")
        time.sleep(2)
        continue