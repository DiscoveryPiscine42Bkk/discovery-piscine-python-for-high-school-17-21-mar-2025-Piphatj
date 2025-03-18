#!/usr/bin/env python3
# float.py

num = str(input("Give me a number: "))
dec = float(num)
decc= dec%1
if decc==0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")