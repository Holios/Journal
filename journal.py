# this is my atempt at a journal project. this will hopefully be useful in
# letting me keep a personal journal in a easy to use format

import sys
import datetime
import time
import os
import function
selection = ""
#--------------------------------------
#main loop

while(True):
    print ("1: Add a journal entry")
    print ("2: exit program")
    selection = input(">")

    if selection == "1":

    questionnaire_format = "\nSelf Questionnaire\n------------\n"

# the program will create a folder structure for saving of files,
# this is where we check for/create the needed year and month folders

        mydir = datetime.datetime.now().strftime('%Y')
        mydir2 = datetime.datetime.now().strftime('%B')

        if os.path.isdir(mydir) == False:
            os.mkdir(mydir)
        os.chdir(mydir)

        if os.path.isdir(mydir2) == False:
            os.mkdir(mydir2)
        os.chdir(mydir2)

# creation of the container for the file in use

        my_file_name = datetime.datetime.now().strftime("%B - %d")
        my_file = open(my_file_name + '.txt', "a")

# asks the user for their current mood and a journal entry

        function.entry("how are you feeling today? (enter in \"x\" alone to exist.)","MOOD: {}  \n------------ \n \n")
        function.entry("what is your journal entry for today? \n(Enter in \"x\" alone to exit.)",f"Journal Entry for {datetime.datetime.now().strftime('%B-%d')}" + " \n\n   {}")

# prints into the file a small formatting piece

        my_file.write(questionnaire_format)

# asks the user a series of questions and inputs the answers formatted into the journal file
        function.entry("What was the best thing that happened today? \n(Enter in \"x\" alone to exit.)","The best thing that happened today was: \n{}\n")
        function.entry("Name one thing you did for someone else today. \n(Enter in \"x\" alone to exit.)","Today I helped someone else by:\n{}\n")
        function.entry("Name one thing you did for yourself today: \n(Enter in \"x\" alone to exit.)","Today I helped myself by:\n{}\n")
        function.entry("Name one thing you learned or accomplished today: \n(Enter in \"x\" alone to exit.)","Today I:\n{}\n")

# closes the file that has been used  and resets the active directory
        my_file.close()

        os.chdir("../..")

# closes the program when "2" is selected
    if selection == "2":
        sys.exit()
