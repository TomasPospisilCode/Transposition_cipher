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
    pass

def Program():
    tupleWithData = UserInput()
    DisplayUserInput(tupleWithData)


Program()