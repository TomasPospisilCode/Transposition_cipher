#!/usr/bin/env

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

#No validation implemented yet
def UserInput():
    message = input("Enter your message: ")
    key = input("Enter your key: ")
    return (message, key)#Cool, multiple data can be returned by tuple

def DisplayUserInput(tupleWithData):
    print("User message: {0}".format(tupleWithData[0]))
    print("User key: {0}".format(tupleWithData[1]))

def DoTheTransposition(message, key):
    table = []
    for x in range(key):#let's make it as two dimensional list, number of column is given by key so it might make 8 column now
        table.append([x])
    currentColumn = 0
    currentRow = 0

    #loops through every character in message
    for character in message:
        table[currentColumn].insert(currentRow,character) #Every character is assigned to new column on the first position in the column
        currentColumn= currentColumn+1
        if currentColumn > 7:#if program fiinish assigning character to last column, it starts with new row
            currentColumn = 0
            currentRow=currentRow+1
    print(table)
def Program():
    tupleWithData = UserInput()
    DisplayUserInput(tupleWithData)
    DoTheTransposition("Common sense is not so common.", 8)


Program()



