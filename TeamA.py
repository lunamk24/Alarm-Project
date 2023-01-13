import ZoomLink
import Genre
import SortingSong
import TimeSet as TS

choice = 3

while choice != "1" and choice != "2":
    choice = input("Enter 1 to set an alarm for a class or 2 for"
                   " a basic alarm: ")
    if choice == "1":
        ZoomLink.zoom_link()

    elif choice == "2":
        link = 3

        while link != "1" and link != "2":
            link = input("Enter 1 to use a youtube link or 2 to"
                         " use a random song: ")

            if link == "1":
                url = input("Enter the youtube link: ")
                TS.checking(url)  # will set time and play video

            elif link == "2":
                Genre.get_genre()  # will get genre, sort songs, set time, and play songs

            else:
                print("Invalid input!")

    else:
        print("Invalid input!")
