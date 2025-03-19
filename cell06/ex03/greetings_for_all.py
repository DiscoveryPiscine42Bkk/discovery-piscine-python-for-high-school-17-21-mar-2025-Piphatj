#!/usr/bin/env python3

def greetings(a=None):
    if a == None or isinstance(a,str) and len(a) != 0:
        print(f"Hello, {a}.")
    elif not isinstance(a,str):
        print("Error! It was not a name.")
    else: 
        print("Hello, noble stranger.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)