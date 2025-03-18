#!/usr/bin/env python3

def greetings(a):
    if len(a)==0:
        return "Hello, noble stranger."
    elif not isinstance(a,str):
        return f"Hello, {a}."
    else:
        return "Error! It was not a name."

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)