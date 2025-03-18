#!/usr/bin/env python3
import sys
if len(sys.argv) !=2:
    print("none")
else :
    pas = input("What was the parameter? ")
    if sys.argv[1] == pas:
        print("Good job!")
    else:
        print("Nope sorry...")