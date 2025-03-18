#!/usr/bin/env python3
# downcase_all.py

import sys

def downcase_it(a):
    return a.lower()

if len(sys.argv)<2:
    print("none")
else:
    for pram in sys.argv[1:]:
        print(downcase_it(pram))