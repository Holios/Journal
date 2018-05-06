# this is my atempt at a journal project. this will hopefully be useful in
# letting me keep a personal journal in a easy to use format

import sys
import datetime
import time
import pickle

class Entry:
    def __init__(self):
        self.mood = ""
        self.text = ""


selection = ""
entries = {}
while(True):
    print ("1: Add a journal entry")
    print ("2: read previous journal entries")
    print ("3: Delete/modify an entry")
    print ("4: exit program")
    selection = input(">")

    if selection == "1":
        time = datetime.datetime.now().strftime("%d-%m-%y-%h")

# check to see if there is a current entry for today
        if (time in entries.keys()):
            print ("there is already a very recent entry")
            print ("do you want to over write the recent entry?")
            overwrite = input("> (Y/N)")
            if overwrite == "Y":
                print ("please enter the new entry")
                entries[time].text = input(">")
                p_out = open("journal.pkl", "wb")
                pickle.dump(entries[time].text, p_out)
            if overwrite == "N":
                print ("returning to main menu")
        else:
            print ("enter your journal entry for today")
            entries[time] = Entry()





    if selection == "2":
        print ("these are the previous entries")
        p_in = open("journal.pkl", "rb")
        returned_entries = pickle.load(p_in)
        print (returned_entries)




    if selection == "4":
        sys.exit()
