try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def Search(query, resultsNum, resultsStop):
    SearchResults = []
    for index, i in enumerate(search(query, tld= "com",num=resultsNum, stop=resultsStop, pause = 2)):
        #print(f"Resource: {i}")
        SearchResults.append(i)
    return SearchResults

#Search(10,10)

