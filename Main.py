# @author Vivek
# @version 1.0
# @since 24-12-2018

import math

documents = ["This little kitty came to play when I was eating at a restaurant.",
             "Merley has the best squooshy kitten belly.",
             "Google indexanslate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

mapOfOverallWordsAndCount = {}
mapOfIndexAndDocumentCountMap = {}
index = 1
for document in documents:
    document = document.replace(".", "")
    document = document.lower()
    words = document.split(" ")

    documentWords = {}
    for word in words:
        if word in documentWords:
            documentWords[word] = documentWords[word] + 1
        else:
            documentWords[word] = 1

        if word in mapOfOverallWordsAndCount:
            mapOfOverallWordsAndCount[word] = mapOfOverallWordsAndCount[word] + 1
        else:
            mapOfOverallWordsAndCount[word] = 1
    mapOfIndexAndDocumentCountMap[index] = documentWords
    index += 1

N = mapOfIndexAndDocumentCountMap.__len__()
for index in mapOfIndexAndDocumentCountMap:
    print(str(index) + " :: " + str(mapOfIndexAndDocumentCountMap[index]))
    print("For document " + str(index) + ":--")
    wordsOfDoc = mapOfIndexAndDocumentCountMap[index]
    countOfWordsInDoc = mapOfIndexAndDocumentCountMap[index].__len__()

    for word in wordsOfDoc:
        # calc of tf here
        termCount = mapOfIndexAndDocumentCountMap[index][word]
        tf = termCount / countOfWordsInDoc
        print("Term freq of " + word + " is : " + str(termCount) + " => " + str(tf))

        # going for idf here - ln(N/(1 + |docs containing the word|))
        docsWithWord = 0
        for internal in mapOfIndexAndDocumentCountMap:
            if word in mapOfIndexAndDocumentCountMap[internal]:
                docsWithWord += 1

        idf = math.log(N / (1 + docsWithWord))
        print("\t\tThe inverse frequency related terms -- N : " + str(N) + ", docs containing the word : " + str(
            docsWithWord) + " ~~ " + str(idf))

        val = tf * idf
        print("\t\t\tValue : " + str(val))

    break

"""
print("displaying the overall map:-")
for word in mapOfOverallWordsAndCount:
    print(word + " -- " + str(mapOfOverallWordsAndCount[word]))
"""
