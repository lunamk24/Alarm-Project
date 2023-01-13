import webbrowser as wb
import re
import sys
import datetime
import time
import ZoomLink
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


def check_link(url):
    link = "youtube"
    watch = "watch"
    try:
        if url.split(".", maxsplit=2)[1] != link:
            raise ValueError
        elif url.split("/")[3][0:5] != watch:
            raise BaseException
    except ValueError as v:
        sys.exit("This is not youtube link")
    except BaseException as b:
        sys.exit("This is youtube link, but with no video.")


def y(x, n):
    if n == 1:
        return int(x) * 3600
    if n == 2:
        return (int(x) * 10) * 60
    if n == 3:
        return int(x) * 60
    if n == 4:
        return int(x) * 10
    if n == 5:
        return int(x)


def check_time(time):
    try:
        check = re.sub(':', '', time)
        for n in time:
            if not (check.isdigit()):
                raise ValueError
    except ValueError:
        sys.exit("This is not valid time")
    sum_time = 0
    index = 1
    for i in time.split(":"):
        if index == 1:
            if int(i[1]) != 0:
                new_time = list(map(y, i[1], [1]))
                sum_time += sum(new_time)
            index += 1
        elif index == 2:
            if int(i[0]) != 0:
                new_time = list(map(y, i[0], [2]))
                sum_time += sum(new_time)
            if int(i[1]) != 0:
                new_time = list(map(y, i[1], [3]))
                sum_time += sum(new_time)
            index += 1
        elif index == 3:
            if int(i[0]) != 0:
                new_time = list(map(y, i[0], [4]))
                sum_time += sum(new_time)
            if int(i[1]) != 0:
                new_time = list(map(y, i[1], [5]))
                sum_time += sum(new_time)
    return sum_time


def play_video(url, set_time):
    new_url = url + '&t=' + str(set_time) + 's'
    wb.open(new_url)


def checking(url):
    check_link(url)
    set_time = input("Enter the time you want to play (00:00:00)    ")
    set_time = check_time(set_time)

    alarm_input = input("\nSet a time for the alarm (Ex. 06:30 or 18:30:00)\n>> ")
    while True:
        try:
            alarm_time = [int(n) for n in alarm_input.split(":")]
            if ZoomLink.check_alarm_input(alarm_time):
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
    print("\nAlarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

    # Sleep until the alarm goes off
    time.sleep(time_diff_seconds)

    play_video(url, set_time)
