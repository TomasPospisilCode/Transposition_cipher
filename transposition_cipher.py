#!/usr/bin/env
import math

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

#Enter cipher and key and you got deciphered message
def Decipher(cipheredText, key):
    rowsOfTable = math.ceil(len(cipheredText) / key)#Get number of rows of table
    decipheredText = ""

    for row in range(rowsOfTable):#Go through every row
        index = row
        for char in cipheredText:
            decipheredText += cipheredText[index]
            index+rowsOfTable





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
    print("Ciphered text: " + cipheredMessage)

def DoTheTransposition(message, key):
    table = []
    for x in range(int(key)):#let's make it as two dimensional list, number of column is given by key so it might make 8 column now
        table.append([])
    currentColumn = 0
    currentRow = 0

    #loops through every character in message
    for character in message:
        table[currentColumn].insert(currentRow,character) #Every character is assigned to it's column
        currentColumn= currentColumn+1
        if currentColumn > int(key)-1:#if program finish assigning character to last column, it starts with new row
            currentColumn = 0
            currentRow=currentRow+1
    return table

def Program():
    tupleWithData = UserInput()#Tuple contains message and key
    message = tupleWithData[0]
    key = tupleWithData[1]

    DisplayUserInput(tupleWithData)
    table = DoTheTransposition(message, key)
    DisplayCipheredText(table)


Program()



