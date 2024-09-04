#!/usr/bin/env python 

s1 = set(map(lambda x: x.rstrip(), open("run1.txt").readlines()))
s2 = set(map(lambda x: x.rstrip(), open("run2.txt").readlines()))

c_elem = s1 & s2
x_1 = s1 - s2
x_2 = s2 - s1

print(x_1) 
print(x_2)
