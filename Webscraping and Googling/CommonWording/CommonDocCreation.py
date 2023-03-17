def WriteToDoc(doc):
    print("placeholder")

def main():
    docName = input("please input document name - \n>\t")
    print(f"writing to the document: {docName}")

    f = open(docName, "a")    
    userInput = ''
    while userInput.lower() != "done":
        userInput = input(f'please enter another item: \n>\t')
        f.write(userInput + ', \n')
    f.close()

main()