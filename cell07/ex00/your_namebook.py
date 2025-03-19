#!/usr/bin/env python3

def array_of_names(name):
    full_name =[]
    for first,last in name.items():
        aname=f"{first.capitalize()} {last}"
        full_name.append(aname)
    return full_name


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))