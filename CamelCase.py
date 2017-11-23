#!/bin/python3

import sys, re


s = input().strip()

print(len([i for i in re.split(r"([A-Z][a-z]*)", s) if i != ""]))



