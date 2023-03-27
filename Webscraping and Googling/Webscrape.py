from bs4 import BeautifulSoup as bs
import requests #needs the library 'requests' (pip install requests)
import time
import Search as S

#SearchResults = (S.Search(10,10))

def TestURL(URL):
    if requests.get(URL) == 200:
        print(requests.get(URL))
        print("connected")
    else:
        print("failure in connection...")

def ResultCount(URL):
    htmlText = requests.get(URL).text
    soup = bs(htmlText, 'lxml')
    stat = soup.find('div', class_= 'result-stats')
    print(f'Following text should be the number of results found: {stat}')

def GoogleScrape(URL,specifier):
    htmlText = requests.get(URL).text
    soup = bs(htmlText, 'lxml')
    jobs = soup.find_all('h3', class_= 'LC20lb MBeuO DKV0Md')

def FindPhotos(ingredient, URL):
    print(f"finding photos regarding {ingredient}")
    htmlText = requests.get(URL).text
    soup = bs(htmlText, 'lxml')
    jobs = soup.find_all('h3', class_= 'LC20lb MBeuO DKV0Md')
    

#def GoogleSearch():
#    SearchResults = (S.Search(10,10))
#    for result in SearchResults:
#        print(f'Scraping - {result}')
#        GoogleScrape(result)


URL = "https://www.google.com/search?q=webpages&rlz=1C1UEAD_enUS970US970&oq=webpages&aqs=chrome..69i57j46i131i199i433i465i512j0i131i433i512j46i131i199i433i465i512j0i433i512j46i10i131i199i433i465j0i131i433i512j46i131i199i433i465i512j0i131i433i512.1331j0j7&sourceid=chrome&ie=UTF-8"
#TestURL(URL)
#ResultCount(URL)


