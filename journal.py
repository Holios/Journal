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
        year_folder = "{datetime.datetime.now().strftime('%Y')}"
        month_folder = "{datetime.datetime.now().strftime('%M')}"
        time = datetime.datetime.now().strftime("%d-%m-%y-%h")
        if os.path.isdir(f'./{datetime.datetime.now().strftime("%Y")}') == False:
            mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime("%Y"))
            os.makedirs(mydir)
        if os.path.isdir(f'./{year_folder} + "\\" + {month_folder}') == False:
            mydir2 = os.path.join(os.getcwd(), datetime.datetime.now().strftime("%Y") + "//" + datetime.datetime.now().strftime('%B'))
            os.makedirs(mydir2)
        if os.path.is
        print("Enter in \"x\" alone to exit.")
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")

    if selection == "2":
        pass
    if selection == "4":
        sys.exit()
