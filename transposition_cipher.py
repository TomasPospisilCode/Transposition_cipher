#!/usr/bin/env
import math
import random
import sys

'''
 _____                                   _ _   _                    _       _
|_   _|                                 (_) | (_)                  (_)     | |
  | |_ __ __ _ _ __  ___ _ __   ___  ___ _| |_ _  ___  _ __     ___ _ _ __ | |__   ___ _ __
  | | '__/ _` | '_ \/ __| '_ \ / _ \/ __| | __| |/ _ \| '_ \   / __| | '_ \| '_ \ / _ \ '__|
  | | | | (_| | | | \__ \ |_) | (_) \__ \ | |_| | (_) | | | | | (__| | |_) | | | |  __/ |
  \_/_|  \__,_|_| |_|___/ .__/ \___/|___/_|\__|_|\___/|_| |_|  \___|_| .__/|_| |_|\___|_|
                        | |                                          | |
                        |_|                                          |_|
'''
def TestingFuction():
    random.seed()#Setting seed
    for i in range(20):#run 20 tests
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4,40)#create message with random length
        message = list(message)#convert message to list
        random.shuffle(message)#shuffle characters in message
        message = ''.join(message)
        print("Test " + str(i+1) + "# " + message)

        for key in range(1, len(message)):
            encrypted_message = DoTheTransposition(message, key)
            decrypted_message = Decipher(encrypted_message, key)


            if message != decrypted_message:
                print("Something gone wrong")
                sys.exit()
    print("Transposition passed")



#Enter cipher and key and you got deciphered message
def Decipher(cipheredText, key):
    numOfColumns = math.ceil(len(cipheredText)/key)
    numOfRows = key

    numOfShadeBoxes = (numOfColumns * numOfRows) - len(cipheredText)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in cipheredText:
        plaintext[col] += symbol
        col += 1#Point to next column

        #If there are no more columns OR we're at a shaded box, go back to the first column and the next row

        if(col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadeBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)


#No validation implemented yet
def UserInput():
    message = input("Enter your message: ")
    key = input("Enter your key: ")
    return (message, key)#Cool, multiple data can be returned by tuple

#Displays user input
def DisplayUserInput(tupleWithData):
    print("User message: {0}".format(tupleWithData[0]))
    print("User key: {0}".format(tupleWithData[1]))

#Displays ciphered text
def DisplayCipheredText(table):
    cipheredMessage = ""
    #Go through every column in table and add characters to ciphered message
    for column in table:
        for character in column:
            cipheredMessage += character
    return cipheredMessage
    #print("Ciphered text: " + cipheredMessage)

def DoTheTransposition(message, key):
    ciphered_message = ""



    for column in range(int(key)):#Every iteration fill in one column
        index = column
        shift = 0

        while index < len(message):

            ciphered_message += message[index]
            shift += key
            index = column + shift
    return ciphered_message


def Program():
    tupleWithData = UserInput()#Tuple contains message and key
    message = tupleWithData[0]
    key = tupleWithData[1]

    DisplayUserInput(tupleWithData)
    table = DoTheTransposition(message, key)
    DisplayCipheredText(table)

TestingFuction()

