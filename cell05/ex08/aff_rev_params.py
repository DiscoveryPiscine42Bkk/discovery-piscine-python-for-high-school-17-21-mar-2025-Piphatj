#!/usr/bin/env python3
# aff_rev_params.py
import sys
if (len(sys.argv)-1)>1:
    reversedp = sys.argv[1:][::-1]
    for param in reversedp:
        print(param)
else:
    print("none")