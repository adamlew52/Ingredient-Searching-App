import cv2
import pytesseract as pytess
pytess.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def testMode(imgList):
    print(imgList)
    for img in imgList:
        #StringParse(ImageReader(img))
        if '.png' or '.jpg' or '.jpeg' in img:
            readImg = StringParse(ImageReader(img))
            #print("\t-----------------Begin-----------------------")
            #print(readImg)
            #print("\t-----------------End-----------------------\n\n")
        else:
            print('Not an accepted image type...')
            pass
    return readImg

#def ImageProcessor(img):
#    readImg = StringParse(ImageReader(img))
#    return readImg

def ImageReader(imgPath):
    img = cv2.imread(imgPath)
    text = pytess.image_to_string(img)
    #print(f"Ingredient List: {text}")
    return text

def StringParse(string):
    #print("Scanning Image...")
    removeIngredientWord = string.split(":")
    try:
        parsedString = removeIngredientWord[1].split(',')
    except:
        print("no listing of the phrase \"Ingredient: \"")
    return parsedString

def RemoveEscapeChar(parsedString):
    print("Looking for escape characters...")
    escapeChar = ["\\n", "\\t", "\\r"]
    for ingredient in parsedString:
        print(ingredient)
        for char in escapeChar:
            print(f"char: {char}")
            if char in ingredient:
                newParsedString = parsedString.replace(char, "-REPLACED ESCAPE CHARACTER-")
                #print(newParsedString)
                return newParsedString
            else:
                pass

def UnitTest():
    #ImageReader(imgPath)
    #print(StringParse(ImageReader(imgPath)))

    imgList = ["TestImages\ingredients.jpeg"]#,"TestImages\Ingredients.png"] #"TestImages\\test.jpg"]
    imgList2 = ["TestImages\Ingredients.png"]
    test = testMode(imgList)
    test2 = testMode(imgList2)
    print(f"test: {test}\n")
    print(f"test2: {test2}")

    # print(RemoveEscapeChar(test)) #TODO