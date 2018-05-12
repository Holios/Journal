# function for multiple calls for similar code. takes two strings

import sys
import datetime
import time
import os

def entry(prompt,formatting):

        my_file_name = datetime.datetime.now().strftime("%B - %d")
        my_file = open(my_file_name + '.txt', "a")

        print(prompt)
        journal = ""
        while(True):
            newline = input(": ")
            if(newline =="x"):
                break
            journal = journal + (newline + "\n")
        journal_entry = (formatting)
        my_file.write(journal_entry)
