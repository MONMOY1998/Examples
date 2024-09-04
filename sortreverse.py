#!/usr/bin/env python 

f = open("run3.txt")
a = list(map(lambda x: float(x.rstrip()), f.readlines()))
f.close()
print(a)
a[:5] = sorted(a[:5])
a[5:] = reversed(a[5:])
print(a)
