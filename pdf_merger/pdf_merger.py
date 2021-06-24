# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:43:19 2020

@author: Louis Lin
"""

from PyPDF2 import PdfFileMerger, PageRange
from csv import reader
from tkinter import Tk
from os import chdir, remove, path
from pathlib import Path

clipboard = Tk().clipboard_get()

if Path(clipboard).exists():
    print("Changing directory to " + clipboard)
    chdir(clipboard)
else:
    print("Assuming the instruction is in current folder")


# Open up the instruction txt file
if Path('./pdf_instructions.txt').exists():
    with open('./pdf_instructions.txt') as instruction:
        # Gets all of the text from instruction
        read = list(reader(instruction, delimiter = ' '))  #Space deliminated instructions
        # Gets all of the pdf needed to be merged  
        pdfList = [inputs for inputs in read[3:len(read)+1] if inputs!=[]] #Skips the first 3 lines and skips blanks
        # Removes the output pdf if it exists
        if path.exists(read[1][0]):
            remove(read[1][0])
        # Name of the output pdf
        output = read[1][0]
        # Merge the PDFs
        with open(output,'wb') as output: # Creates the output pdf
            # Creates a merger object from PyPDF2
            mergerObj = PdfFileMerger(strict=False)
            i = 0 # Counter for going through the PDF list
            while i < len(pdfList):
                filename = pdfList[i] # Current pdf
                if Path(filename[0]).exists(): # Makes sure the pdf path is correct 
                    print("Merging " + filename[0])
                    if len(filename) == 1: # Appends the entire PDF
                        bookmark_name = path.basename(filename[0]).split('.')[0] # Bookmark Name
                        mergerObj.addBookmark(bookmark_name, len(mergerObj.pages)) # Adds a bookmark
                        mergerObj.append(filename[0]) # Adds the file
                    else: 
                        mergerObj.append(filename[0], pages = PageRange(filename[1])) # Have the 
                # Maybe you forgot the extension !?
                else: # Dummy proofing for myself
                    if Path(filename[0] +'.pdf').exists():
                        filename[0] = filename[0]+'.pdf' # Checks if there's a pdf
                        print("Merging " + filename[0]) # Opens it
                        if len(filename) == 1: # Same as before
                            bookmark_name = path.basename(filename[0]).split('.')[0]
                            mergerObj.addBookmark(bookmark_name, len(mergerObj.pages))
                            mergerObj.append(filename[0])
                        else: 
                            mergerObj.append(filename[0], pages = PageRange(filename[1]))
                    # You messed up and the file does not exist
                    else:   
                        print("Error with "+filename[0])
                        break
                i = i +1
            # Print the pdf
            mergerObj.write(output)
else:
    print("Missing Instructions!")