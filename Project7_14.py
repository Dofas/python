#! /usr/bin/env python3
import re


def check(text):
    if not text.strip():
        return True

    return re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b', text) is not None

s=input('Vvedit6 email ')

print(check(s))

