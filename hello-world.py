import time

string = "Hello World"

def type(string):
    for letter in string:
        print(letter, end="", flush=True)
        time.sleep(.2)

type(string)