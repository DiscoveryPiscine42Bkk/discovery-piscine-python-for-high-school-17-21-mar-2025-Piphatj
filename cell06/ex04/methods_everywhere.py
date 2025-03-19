#!/usr/bin/env python3

import sys

def shrink(a):
    x=a.ljust(8,"Z")
    print(x)
def enlarge(a):
    print(a[:8])
if len(sys.argv)<2:
    print("none")
for a in sys.argv[1:]:
    if len(a)>8:
        enlarge(a)
    elif len(a)<=8:
        shrink(a)
    