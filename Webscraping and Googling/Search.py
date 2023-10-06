try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def Search(query, resultsNum):
    SearchResults = []
    count = 0
    try:
        for index, i in enumerate(search(query, num_results=resultsNum, lang="en", proxy=None, advanced=False, sleep_interval=0, timeout=5)):
            count += 1
            print(f"{count}\t:\tResource: {i}")
            #SearchResults.append(i)
        return SearchResults
    except Exception as e:
        print(e)
