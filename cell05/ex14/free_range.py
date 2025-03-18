#!/usr/bin/env python3
import sys,numpy as np
if len(sys.argv) != 3:
    print("none")
else:
    start=int(sys.argv[1])
    stop=int(sys.argv[2])+1
    ar = list(range(start,stop))
    print(ar)