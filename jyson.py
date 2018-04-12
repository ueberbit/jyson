#!/usr/bin/python3

import sys,json

input = sys.stdin
args  = sys.argv[1:]
depth = len(args)

json_object = json.load(input)

for i in range(0, depth):
  json_object = json_object[args[i]]

print(json_object)
