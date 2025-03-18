#!/usr/bin/env python3
# i_got_that.py
i=0
say = input("What you gotta say? : ")
while i == 0:
    say = input("I got that! Anything else? : ")
    if say =="STOP":
        break
        i +=1