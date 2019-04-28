#! /usr/bin/python3
import re

word = "aureliusz"
output = []

def init (word):
    length = len(word)
    for i in range(length):
        output.append('_')

def update(letter, reference):
    for i in reference:
        output[i] = letter


def find_word(letter, word):
    out =  [x.start() for x in re.finditer(letter, word)]
    return out

def print_panel(output):
        for i in output: 
                print(i, end="")
        

def Hangman(word):
    reference = []
    while True:
        letter = input("\nWrite letter: ")
        reference = find_word(letter,word)
        if reference:
            update(letter,reference)
            break

def check(output):
    if '_' in output:
        return False
    else:
        print("\n Wygrałeś")
        return True
init(word)
   
while True:
    print_panel(output)
    Hangman(word)
    if check(output):
        break
        
