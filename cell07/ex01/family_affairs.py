#!/usr/bin/env python3

def find_the_redheads(a):
    name=[]
    for f,s in a.items():
        if s=="red":
            name.append(f)
    return name
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))