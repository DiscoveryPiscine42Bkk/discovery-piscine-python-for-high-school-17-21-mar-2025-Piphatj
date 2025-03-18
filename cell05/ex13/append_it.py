#!/usr/bin/env python3
import sys
if len(sys.argv)<2:
    print("none")
else:
    for pram in sys.argv[1:]:
        if not pram.endswith("ism"):
            print(f"{pram}ism")
