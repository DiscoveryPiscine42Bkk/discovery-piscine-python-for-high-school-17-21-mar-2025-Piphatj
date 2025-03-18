#!/usr/bin/env python3
# scan_it.py
import sys
import re
if len(sys.argv) >2:
    keyword=sys.argv[1]
    search=sys.argv[2]
    matched=re.findall(keyword,search)
    if len(matched)>0:
        print(len(matched))
    else:
        print("none")
else:
    print("none")