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
        journal_entry = ""
        mood = ""
        mood_entry = ""
        questionnaire_format = "\nSelf Questionnaire\n------------\n"

        mydir = datetime.datetime.now().strftime('%Y')
        mydir2 = datetime.datetime.now().strftime('%B')

        if os.path.isdir(mydir) == False:
            os.mkdir(mydir)

        os.chdir(mydir)

        if os.path.isdir(mydir2) == False:
            os.mkdir(mydir2)

        os.chdir(mydir2)

        my_file_name = datetime.datetime.now().strftime("%B - %d")
        my_file = open(my_file_name + '.txt', "a")

        print("how are you feeling today? (Enter in \"x\" alone to exit.)")
        while (True):
            mood_new_line = input(": ")
            if(mood_new_line == "x"):
                break
            else: mood = mood + (mood_new_line + "\n")
        mood_entry = (f"MOOD: {mood}  \n------------ \n \n")
        my_file.write(mood_entry)

        print("what is your journal entry for today? \n(Enter in \"x\" alone to exit.)")
        journal = ""
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")
        journal_entry = (f"Journal Entry for {datetime.datetime.now().strftime('%B-%d')} \n\n   {journal}")
        my_file.write(journal_entry)

        my_file.write(questionnaire_format)

        print("What was the best thing that happened today? \n(Enter in \"x\" alone to exit.)")
        journal = ""
        while(True):
            newline = input(": ")
            if(newline =="x"):
                break
            else: journal = journal + (newline + "\n")
        journal_entry = (f"The best thing that happened today was: \n{journal}\n")
        my_file.write(journal_entry)

        print("Name one thing you did for someone else today. \n(Enter in \"x\" alone to exit.)")
        journal = ""
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")
        journal_entry = (f"Today I helped someone else by:\n{journal}\n")
        my_file.write(journal_entry)

        print("Name one thing you did for yourself today: \n(Enter in \"x\" alone to exit.)")
        journal = ""
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")
        journal_entry = (f"Today I helped myself by:\n{journal}\n")
        my_file.write(journal_entry)

        print("Name one thing you learned or accomplished today: \n(Enter in \"x\" alone to exit.)")
        journal = ""
        while(True):
            newline = input(": ")
            if(newline=="x"):
                break
            else: journal = journal + (newline + "\n")
        journal_entry = (f"Today I:\n{journal}\n")
        my_file.write(journal_entry)
        my_file.close()

        os.chdir("../..")

    if selection == "4":
        sys.exit()
