# function for multiple calls for similar code. takes two strings

import sys
import datetime
import time
import os

def entry(prompt,formatting):
# sets the file name and a container for the file
        my_file_name = datetime.datetime.now().strftime("%B - %d")
        my_file = open(my_file_name + '.txt', "a")

# runs through a prompt sent to screen and lets the user input an entry based
# upon the prompt, formats the entry and appends the entry to a file

        print(prompt)
        journal = ""
        while(True):
            newline = input(": ")
            if(newline =="x"):
                break
            journal = journal + (newline + "\n")
        journal_entry = formatting.format(journal)
        my_file.write(journal_entry)
