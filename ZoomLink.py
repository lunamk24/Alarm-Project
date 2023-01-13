import datetime
import os
import time
import random
import webbrowser

# If video URL file does not exist, create one
if not os.path.isfile("subjectZoomList.txt"):
    print('Creating "subjectZoomList.txt"...')


def show_list():
    f = open("subjectZoomList.txt", "r")
    if f.mode == "r":
        myList = f.read()
        print(myList)


def get_inputs():
    while True:
        print("\n== Enter the number that you want to do ==")
        print("1. Select your subject")
        print("2. Add another link")
        print("3. Show the list again")
        print("4. Exit\n")
        option = int(input(">> "))
        if option == 4:
            print("Close the program. Bye!")
            break

        elif option == 1:
            subject = int(input("\nEnter your subject number you want to set alarm\n>> "))
            num_lines = sum(1 for line in open('subjectZoomList.txt'))
            if subject <= num_lines:
                # Get user input for the alarm time
                alarm_input = input("\nSet a time for the alarm (Ex. 06:30 or 18:30:00)\n>> ")
                while True:
                    try:
                        alarm_time = [int(n) for n in alarm_input.split(":")]
                        if check_alarm_input(alarm_time):
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("ERROR: Enter time in HH:MM or HH:MM:SS format")

                # Convert the alarm time from [H:M] or [H:M:S] to seconds
                seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
                alarm_seconds = sum([a * b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

                # Get the current time of day in seconds
                now = datetime.datetime.now()
                current_time_seconds = sum([a * b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])

                # Calculate the number of seconds until alarm goes off
                time_diff_seconds = alarm_seconds - current_time_seconds

                # If time difference is negative, set alarm for next day
                if time_diff_seconds < 0:
                    time_diff_seconds += 86400  # number of seconds in a day

                # Display the amount of time until the alarm goes off
                print("\nYou are all set!!")
                print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

                # Sleep until the alarm goes off
                time.sleep(time_diff_seconds)

                # Time for the alarm to go off
                print("Wake Up!")

                # Load list of possible URLs
                f = open('subjectZoomList.txt', "r")
                all_lines_variable = f.readlines()
                line = all_lines_variable[subject - 1]
                # print(line)
                line = line.split(" ")
                link = line[1]
                # print(link)
                webbrowser.open(link)

                print("Do you want to continue ? (Y/N)")
                choice = input(">>")

                if choice == "N":
                    break

                else:
                    if not line: break

        elif option == 2:
            f = open("subjectZoomList.txt", "a+")
            add = input("Enter a new link (\"Subject, link\" format) : ")
            f.write("\n")
            f.write(add)
            f.close()

        elif option == 3:
            f = open("subjectZoomList.txt", "r")
            if f.mode == "r":
                myList = f.read()
                print("\n", myList)

        else:
            print("Error! Please enter the number between 1-4.")


def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1:  # [Hour] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2:  # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3:  # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False


def zoom_link():
    show_list()
    get_inputs()