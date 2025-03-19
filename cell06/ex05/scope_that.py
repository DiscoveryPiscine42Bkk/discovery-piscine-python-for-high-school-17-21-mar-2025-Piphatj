#!/usr/bin/env python3

def add_one(a: int) -> None:
    a += 1
    print(f"add_one(): {a}")

var=2
print(f"Before :{var}")
add_one(var)