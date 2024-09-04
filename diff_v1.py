#!/usr/bin/env python 

lines_1 = open("run1.txt").readlines()
lines_2 = open("run2.txt").readlines()

numbers_1 = []
for item in lines_1:
    numbers_1.append(item.rstrip())

numbers_2 = []
for item in lines_2:
    numbers_2.append(item.rstrip())

s1 = set(numbers_1)
s2 = set(numbers_2)

c_elem = s1 & s2
x_1 = s1 - s2
x_2 = s2 - s1

print (x_1) 
print (x_2)
