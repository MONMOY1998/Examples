#!/usr/bin/env python3
f = open('players.csv', 'r') # r -> read
for line in f:
  line = line.strip()
  fields = line.split(",")
  if fields[1] == 'India':
    print(line)
f.close()
