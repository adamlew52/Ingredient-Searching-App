import os
from os import walk
from pathlib import Path
import sqlite3 as sl3


def WriteToDoc(doc):
    print("placeholder print statement...")

def SelectDoc():
    applicable = GetDocInfo()

    counter = 0
    for files in applicable:
        counter += 1
        print(f'{counter}. {files}')
    
    print(applicable)
    
    userInput = input("Please select the file you would like to write to\n>\t")
    
    try:
        userInput = int(userInput) - 1
        if type(userInput) == int:
            return  applicable[userInput]
        else:
            SelectDoc()
    except:
        GetDocInfo()

def GetDocInfo():
    cwd = os.path.abspath('Webscraping and Googling\CommonWording')
    filenames = next(walk(cwd), (None, None, []))[2]  # [] if no file
    applicable = []
    for file in filenames:
        if '.txt' in file:
            applicable.append(file)
        else:
            pass

    return applicable

def main():
    docName = (f'Webscraping and Googling\CommonWording\{SelectDoc()}') #input("please input document name - \n>\t")
    #print(f"writing to the document: {SelectDoc()}")

    print(f'now writing to document..........')

    f = open(docName, "a")    
    userInput = ''
    while userInput.lower() != "done":
        userInput = input(f'please enter another item: \n>\t')
        if userInput.lower() != 'done':
            f.write(userInput + ', \n')
        else:
            break
    f.close()


main()