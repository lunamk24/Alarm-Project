import sys
import LinkedList


def sort_songs(filename):
    with open(filename, "r+") as alarm_file:
        for line in alarm_file:
            line = line.rstrip("\n")
            current_line = line.split(",")
            if song_list.get_length() == 0 or current_line[0].lower() <= (song_list.get_first_title()).lower():
                song_list.add_first(current_line[0], current_line[1])
            elif song_list.get_length() == 1 or current_line[0].lower() > (song_list.get_last_title()).lower():
                song_list.add_last(current_line[0], current_line[1])
            else:
                song_list.place_iterator()
                for i in range(song_list.get_length() - 1):
                    if current_line[0].lower() > (song_list.get_iterator_title()).lower():
                        song_list.advance_iterator()
                    else:
                        break
                song_list.reverse_iterator()
                song_list.add_iterator(current_line[0], current_line[1])

        song_list.place_iterator()
        alarm_file.seek(0)
        alarm_file.truncate()
        for j in range(song_list.get_length()):
            alarm_file.write(song_list.get_iterator_title() + "," + song_list.get_iterator_link() + "\n")
            song_list.advance_iterator()


song_list = LinkedList.DoublyLinkedList()

#sort_songs("song_list.txt")
#song_list.print_numbered_list()
