#!/usr/bin/env python3
# to25.py
n=10
for i in range(0,n+1):
    print("Table de ",i,": ",end=" ")
    for j in range(0,11):
        print(i*j,end=" ")
    print()