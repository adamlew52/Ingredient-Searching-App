import urllib.request
import Search as s
import Webscrape as w
import webbrowser as wb
import tldextract as tld
import WebpageProcessing as wp
from bs4 import BeautifulSoup as bs
import Image_Processing as imgproc

def GoogleIngredient(ingredient, useCase):
    searchCrit = ingredient
    searchCrit += useCase
    #print(f"Search Criterion: {searchCrit}")
    results = 2 #change me for more or less sources

    print(f'finding {results} resources on{ingredient}...')
    resultsNum = results
    try:
        sourceList = s.Search(searchCrit, resultsNum)
    except Exception as e:
        print(f"Process Failed. Failure protocol {e}")
    return sourceList

def Search_From_Photo(imgPath):
    imgPathParsed = imgproc.testMode(imgPath)
    print(f"\t\t\tParsed from Image: \n\n{imgPathParsed}")
    for ingredient in imgPathParsed:
        print(f"\t\t\tIngredient: {ingredient}")
        SourceList = GoogleIngredient(ingredient, " ")
        print(f"\t\t\tSourceList: {SourceList}")

imgList = ["TestImages\Ingredients.png"]
Search_From_Photo(imgList)
