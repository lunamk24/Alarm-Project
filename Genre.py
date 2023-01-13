import datetime
import os
import time
import random
import webbrowser
import SortingSong
from random import *
import LinkedList
import TimeSet


# Get user input for the alarm file


# Asking genre
def genre_choosing(genre1):
    if genre1 == 1:
        alarm_file = "Jazz.txt.txt"
    elif genre1 == 2:
        alarm_file = "Pop.txt.txt"
    elif genre1 == 3:
        alarm_file = "Classic.txt.txt"

    SortingSong.sort_songs(alarm_file)

    i=0

    while True:

        songs = open(alarm_file, "r")
        # read the file by lines -> line = title of the song, link
        all_lines = songs.readlines()
        line = all_lines[i]
        #moving to the next song

        # print(line) - checking if line worked or not

        # By spliting the line into two parts, video_link = [title of the song, link]
        video_link = line.split(',')

        # print(video_link) - this is for checking
        # print(video_link[1]) - this is for checking & video[1] is where the link saved

        TimeSet.checking(video_link[1])

        print("Do you want to continue ? (Y/N)")
        choice = input(">>")

        if choice == "N":
            break

        else:
            i = i +1
            if not line: break



# Checking input
def get_genre():
    print("Please select the genre, it will play automatically")
    print("=" * 40)
    print("1. Jazz Music")
    print("2. Pop Music")
    print("3. Classic music")
    print("Other numbers for random music")
    print("=" * 40)
    genre = int(input("Enter your choice: "))

    if genre >= 4:
        genre = randint(1, 3)

    genre_choosing(genre)
