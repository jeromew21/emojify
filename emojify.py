#!/usr/bin/python
import emoji
import random
import sys

all_emojis = list(emoji.UNICODE_EMOJI.keys())

def random_emoji():
    a = random.choice(all_emojis)
    #while '\u200d' in a:
     #   a = random.choice(all_emojis)
    return a

def tokenize(sentence):
    return sentence.split(" ")

def append_emoji(word):
    return "{0} {1} ".format(word, random_emoji())

def emojify(sentence):
    tokens = tokenize(sentence)
    return random_emoji() + " " + " ".join(map(append_emoji, tokens))

def echo():
    while True:
        a = input()
        print(emojify(a))
        
if __name__ == "__main__":
    echo()