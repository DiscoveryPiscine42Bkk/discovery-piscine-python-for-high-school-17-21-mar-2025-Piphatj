#!/usr/bin/env python3
import sys
if len(sys.argv)!=2:
    print("none")
else:
    keyz=sys.argv[1]
    if "z" in keyz:
        for char in keyz:
            if char =="z":
                print("z",end="")
    else:
        print("none")