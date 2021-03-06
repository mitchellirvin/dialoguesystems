from __future__ import division
import re
from collections import Counter
from itertools import tee, islice
from nltk.tokenize import word_tokenize
import csv, os

text_file = open("script.txt", mode="r")
linkedsentences = list(text_file)


# define a function to count the special characters in a string
def countSpecialChar(line):
    specialChar = 0
    words = word_tokenize(line) # create an array of "words" from the input string.
                                # this function counts special characters/punctuation as words
    for word in words:  # iterate through the array to count special characters/punctuation
        if word.startswith(".") or word.startswith("?") or word.startswith(",") or word.startswith('"') or \
                word.startswith(":") or word.startswith("'") or word.startswith("-") or word.startswith("+") \
                or word.startswith("=") or word.startswith("@") or word.startswith("#") or word.startswith("%") \
                or word.startswith('(') or word.startswith(')'):
            specialChar += 1

    return specialChar

# define a function to count the number of white spaces in a string
def countWhiteSpace(line):
    whiteSpace = 0
    lineToCheck = list(line)    # parse the input line into a list of characters
    for char in lineToCheck:    # iterate through the list to count the number that are white space
        if char == " ":
            whiteSpace += 1
    return whiteSpace


# below is the functionality that allows for finding the most common word
def getCommonToken(script):
    words = re.findall(r'\w+', script)
    cap_words = [word.upper() for word in words]
    word_counts = Counter(cap_words)
    keyVal = getFirstItem(word_counts)
    print("The most common token is: " + str(keyVal[0]) + ", with " + str(keyVal[1]) + " occurrences.")


def getCommonBigram():
    words = re.findall('\w+', open('script.txt').read())
    word_counts = Counter(zip(words, words[1:]))
    keyVal = getFirstItem(word_counts)
    print("The most common bigram is: " + str(keyVal[0]) + " with " + str(keyVal[1]) + " occurrences.")


def getNgrams(script):
    keyVal = getFirstItem(Counter(ngramify(script, 3)))
    print("The most common trigram is: " + str(keyVal[0]) + " with " + str(keyVal[1]) + " occurrences.")


def ngramify(lst, n):
    words = re.findall("\w+", lst)
    tlst = words
    while True:
        a, b = tee(tlst)
        l = tuple(islice(a, n))
        if len(l) == n:
            yield l
            next(b)
            tlst = b
        else:
            break


def getFirstItem(dict):
    maxvalue = 0
    maxkey = ""
    for item in dict.iteritems():
        if item[1] > maxvalue:
            maxvalue = item[1]
            maxkey = item[0]
    return maxkey, maxvalue


# define variables necessary to define the two speakers
count = 0
interlocutor1 = ""
interlocutor2 = ""

# iterate through each "sentence" of the file, where sentence is an utterance by one of the speakers
for sentence in linkedsentences:
    if len(word_tokenize(sentence)) != 0:
        if count == 0:
            interlocutor1 = word_tokenize(sentence)[0]  # assign the first speaker's name to interlocutor1
        elif count == 2:
            interlocutor2 = word_tokenize(sentence)[0]  # assign the second speaker's name to interlocutor2
        elif count > 2:
            break   # once both names have been assigned, break
    count += 1

# number of turns each speaker has taken
turns1 = 0
turns2 = 0
# number of words each speaker has uttered
totalWords1 = 0
totalWords2 = 0

sentenceWords1 =0
sentenceWords2 =0

# sum of characters in all words a speaker has spoken
totalWordLength1 = 0
totalWordLength2 = 0
# number of utterances containing "you" by each speaker
uttersContaining1 = 0
uttersContaining2 = 0
# number of utterances not containing "you" by each speaker
uttersNotContaining1 = 0
uttersNotContaining2 = 0
# variables to track '' in utterances
wordToTrack = "money"
trackUtters = 0
# variables to separate utterances into two arrays, one for each speaker
speaker1Utterances = ""
speaker2Utterances = ""

speaker1Counts = list()
speaker2Counts = list()

tuplist = list()

# iterate through each utterance
for sentence in linkedsentences:
    if sentence.startswith(interlocutor1):  # if the speaker was interlocutor1
        speaker1Utterances += sentence # add the sentence to the list of speaker 1's lines


        turns1 += 1
        totalWords1 = totalWords1 + len(word_tokenize(sentence)) - 1  # Minus two from the name
        totalWords1 = totalWords1 - countSpecialChar(sentence)

        totalWordLength1 = totalWordLength1 + (len(list(sentence))) - countWhiteSpace(sentence) - \
            countSpecialChar(sentence) - (len(interlocutor1) + 1)  # subtracting one more b/c \n char

        # The number of words in each sentence for Speaker 1
        sentenceWords1 = (len(word_tokenize(sentence))) - countSpecialChar(sentence) - 1  # "1" comes from the speaker name
        print(sentenceWords1)

        speaker1Counts.append(sentenceWords1)


        # count the number of utterances containing our chosen word, and not containing
        for word in word_tokenize(sentence):
            if word.startswith(wordToTrack):
                trackUtters += 1
                break

        if trackUtters == 1:
            uttersContaining1 += 1
            tuplist.append(("Speaker1", 1))
        else:
            uttersNotContaining1 += 1
            tuplist.append(("Speaker1", 0))
        trackUtters = 0

        # search for unigrams, bigrams, and n-grams with 'zip'
        # words = re.findall('\w+', sentence)
        # print(Counter(zip(words, words[1:])))



    elif sentence.startswith(interlocutor2):    # if the speaker was interlocutor2
        speaker2Utterances += sentence  # add the sentence to the list of speaker 2's lines
        turns2 += 1
        totalWords2 = totalWords2 + len(word_tokenize(sentence)) - 1  # Minus two from the name
        totalWords2 = totalWords2 - countSpecialChar(sentence)
        totalWordLength2 = totalWordLength2 + (len(list(sentence))) - countWhiteSpace(sentence) - \
            countSpecialChar(sentence) - (len(interlocutor2) + 1) # subtracting one more b/c \n char

        # The number of words in each sentence for Speaker 2
        sentenceWords2 = (len(word_tokenize(sentence))) - countSpecialChar(sentence) - 1  # "1" comes from the speaker name
        print(sentenceWords2)

        # Store the wordcount of each sentence in a list
        speaker2Counts.append(sentenceWords2)

        for word in word_tokenize(sentence):
            if word.startswith(wordToTrack):
                trackUtters += 1
                break

        if trackUtters == 1:
            uttersContaining2 += 1
            tuplist.append(("Speaker2", 1))
        else:
            uttersNotContaining2 += 1
            tuplist.append(("Speaker2", 0))
        trackUtters = 0

print("\n")

print("How many dialogue turns did each interlocutor make?")
print(interlocutor1, ": ", turns1)
print(interlocutor2, ": ", turns2)

print("---------------------------------------------------")
print("How many total words did each interlocutor say?")
print(interlocutor1, ": ", totalWords1)
print(interlocutor2, ": ", totalWords2)


print("---------------------------------------------------")
print("How many words per turn on average did each interlocutor make?")

print(interlocutor1, ": ", totalWords1/turns1)
print(interlocutor2, ": ", totalWords2/turns2)


print("---------------------------------------------------")
print("What is the average length of word that each interlocutor made?")

print(interlocutor1, ": ", totalWordLength1/totalWords1)
print(interlocutor2, ": ", totalWordLength2/totalWords2)

totalContaining = uttersContaining2 + uttersContaining1
totalNotContaining = uttersNotContaining2 + uttersNotContaining1

print("\n---------------------------------------------------\nBEGIN HW 2")
print("\t\t\t\tw/ " + wordToTrack + "\t\t\tw/o  " + wordToTrack + "\t\t\tTotal")
print("Sp. 1\t\t\t" + str(uttersContaining1) + "\t\t\t\t\t" + str(uttersNotContaining1) + "\t\t\t\t\t" + str(turns1))
print("Sp. 2\t\t\t" + str(uttersContaining2) + "\t\t\t\t\t" + str(uttersNotContaining2) + "\t\t\t\t\t" + str(turns2))
print("Total \t\t\t" + str(uttersContaining2 + uttersContaining1) + "\t\t\t\t\t" +
      str(uttersNotContaining1 + uttersNotContaining2) + "\t\t\t\t\t" + str(turns1 + turns2))

with open('script.txt') as f:
    passage = f.read()

print("\n\n")
print("-"*30)
print("SEQUENCE ANALYSIS")
print("-"*30)
print("\nOverall:")
getCommonToken(passage)

print("For " + interlocutor1 + ":")
getCommonToken(speaker1Utterances)

print("For " + interlocutor2 + ":")
getCommonToken(speaker2Utterances)

getCommonBigram()

getNgrams(passage)

text_file.close()

# Printing the word counts to the csv file
print("Writing output file...")
with open('a.csv', 'w') as wordCounts:
    wordCounts.write("Counts,Speaker\n")
    printline = ""

    for value in speaker1Counts:
        printline = str(value) + ",1\n"
        wordCounts.write(printline)
        printline = ""

    for value in speaker2Counts:
        printline = str(value) + ",2\n"
        wordCounts.write(printline)
        printline = ""

    print("Done!")


# Printing the number of utterances containing "money" to the csv file
print("Writing output file...")
with open('b.csv', 'w') as countMoney:
    countMoney.write("Speaker,ContainsMoney\n")
    printline = ""

    for value in tuplist:
        printline = str(value[0]) + "," +str(value[1]) + "\n"
        countMoney.write(printline)
        printline = ""

    print("Done!")
