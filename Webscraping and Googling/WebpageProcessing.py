import os
from os import walk


# make something that searches the sources for the keywords given in the Common Word document
# retrieve the frequency of each type of element
# add these elements to the priorityElements array in the order of frequency
priorityElements = []

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


def ReadCommonWordDoc():
    files = GetDocInfo()
    
    for file in files:
        fileName = files[file]
        docName = (f'Webscraping and Googling\CommonWording\{fileName}')
        print(f'opening {file} the search source material')
        CommonWordSearch(file)

    with open(docName) as f:
        lines = f.readlines()
    return lines

def CommonWordSearch(document):
    print("searching the source documents for the keywords: ")

def KeywordFrequency():
    print("Finding the frequency of the words...")

print(ReadCommonWordDoc())