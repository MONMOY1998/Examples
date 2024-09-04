#!/usr/bin/env python
import copy
w = ['Perl', 'Python', 'Ruby']
c0 = w
c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
c5 = [e for e in w]
c6 = []
for e in w:
    c6.append(e)
c7 = []
c7.extend(w)
print("-> Before update\nc0: ", c0, "\nc1: ", c1, 
"\nc2: ", c2, "\nc3: ", c3, "\nc4: ", c4, 
"\nc5: ", c5, "\nc6: ", c6, "\nc7: ", c7)
w.extend(['Julia','R','Raku'])
print("-> After update\nc0: ", c0, "\nc1: ", c1, 
"\nc2: ", c2, "\nc3: ", c3, "\nc4: ", c4, 
"\nc5: ", c5, "\nc6: ", c6, "\nc7: ", c7)
