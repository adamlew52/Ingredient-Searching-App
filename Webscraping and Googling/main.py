import urllib.request
import Search as s
import Webscrape as w
import webbrowser as wb
import tldextract as tld
import WebpageProcessing as wp

#start data processing---------------------------------------------------------------------------------
def GoogleIngredient(ingredient, useCase):
    searchCrit = ingredient
    searchCrit += useCase
    print(searchCrit)

    print(f'finding resources on {ingredient}...')
    resultsNum = 10
    resultsStop = 10
    sourceList = s.Search(searchCrit,resultsNum, resultsStop)
    #print(f'The following resources were found for {ingredient}:\n{sourceList}')
    #print(type(sourceList))
    return sourceList

def ReadWebpage(URL):
    #print(wb.open(str(URL)))
    try: 
        webUrl = urllib.request.urlopen(URL)
        print("result code: " + str(webUrl.getcode()))
        data = webUrl.read()
        #print(data)
    except:
        print("failed to access the website successfully (see whatever code was found in the error doc)...")
        pass

def OpenWebpage(URL):
    wb.open(URL)  

def CheckRepeatURL(URL, SourceList):
    parsedUrl = tld.extract(URL)
    print(f'URL: {parsedUrl[1]}')

    URL=URL.split(" ")
 
    flag=0
    for i in URL:
        for j in SourceList:
            if i==j:
                flag=1
                break

    if flag==1:
        containSubdomain = True
    else:
        containSubdomain = False
    

    #print("Does string contain any list element : "     + str(bool(res)))
    return containSubdomain

#end data processing------------------------------------------------------------------------------------ 


#start search criterion---------------------------------------------------------------------------------
def findBodyEffects(ingredient):
    print(f'Finding the effects that {ingredient} has on the body...')
    content = GoogleIngredient(ingredient, '\'s effect on the body')
    return content

def findFoodEffects(ingredient):
    print(f'Finding the effects that {ingredient} has on the food item...')
    content = GoogleIngredient(ingredient, '\'s effect on food')
    return content

def findChemicalComp(ingredient):
    print(f'Finding the Chemical Composition of {ingredient}...')
    content = GoogleIngredient(ingredient, '\'s chemical composition')
    return content

def findPosNeg(ingredient):
    print(f'Finding the Positive and Negative effects of {ingredient}...')
    positives = GoogleIngredient(ingredient, '\'s positives')
    negatives = GoogleIngredient(ingredient, '\'s negatives')
    return positives, negatives

def findUses(ingredient):
    print(f'Finding the uses of {ingredient}...')
    content = GoogleIngredient(ingredient, '\'s uses')
    return content

def findOtherNames(ingredient):
    print(f'Finding other names for {ingredient}...')
    content = GoogleIngredient(ingredient, '\'s other names')
    return content
#end search criterion---------------------------------------------------------------------------------


def main():
    ingredient = "niacin"
    #ingredient = input("please input ingredient: \n>")
    #SourceList = (GoogleIngredient(ingredient)) #main

    SourceList = findBodyEffects(ingredient)
    wb.open_new("https://www.google.com/")  
    print("---------------------------------------------------------------------------------")
    for source in SourceList:
        print(f'Finding info from: {source}')
        #ReadWebpage(source)
        #OpenWebpage(source)
        #print(f'was the string contain the element?....................................... {CheckRepeatURL(source, SourceList)}')
    print("---------------------------------------------------------------------------------")

def UnitTest():
    ingredient = "niacin"
    print(f'performing unit testing...\n')

    #SourceList = findBodyEffects(ingredient)
    SourceList = findFoodEffects(ingredient)
    #SourceList = findChemicalComp(ingredient)
    #SourceList = findPosNeg(ingredient)
    #SourceList = findUses(ingredient)
    for source in SourceList:
        print(f'Finding info from: {source}')
        #ReadWebpage(source)
        OpenWebpage(source)
        #print(f'was the string contain the element?....................................... {CheckRepeatURL(source, SourceList)}'
    print("---------------------------------------------------------------------------------")

    
UnitTest()