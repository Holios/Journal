# this is my atempt at a journal project. this will hopefully be useful in
# letting me keep a personal journal in a easy to use format

import sys
import datetime
import time
import os

class Entry:
    def __init__(self):
        self.mood = ""
        self.text = ""


selection = ""

while(True):
    print ("1: Add a journal entry")
    print ("2: read previous journal entries")
    print ("3: Delete/modify an entry")
    print ("4: exit program")
    selection = input(">")

    if selection == "1":
# will create a local folder for year, and sub folders for months, will auto
# create new monthly folders and will create a file with input from the user
# will use the datetime year and datetime month to ensure it is saving entries
# to a searchable folder structure of year(folder) > month(subfolder) > entry(file)
# entry will be listed by date and hour, if there is an entry within the last hour
# todo: will ask the user to either rename, or overwrite

        journal = ""
        mydir = datetime.datetime.now().strftime('%Y')
        mydir2 = datetime.datetime.now().strftime('%B')

        if os.path.isdir(mydir) == False:
            os.mkdir(mydir)

        os.chdir(mydir)

        if os.path.isdir(mydir2) == False:
            os.mkdir(mydir2)

        os.chdir(mydir2)

        my_file_name = datetime.datetime.now().strftime("%B - %d")
        my_file = open(my_file_name + '.txt', "w")
        print("Enter in \"x\" alone to exit.")
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")
        my_file.write(journal)
        my_file.close()

        os.chdir("../..")

    if selection == "2":
        pass
    if selection == "4":
        sys.exit()
