#!/usr/bin/env python

import pprint

sentence = '''
Truth can be stated in a thousand different ways, yet each one can be true.
'''

words = sentence.split()

print (">>> Use map ...")
newlist = list(map(lambda w: [w,w.upper(),len(w)], words))
pprint.pprint(newlist, depth=2)

print (">>> Use List Comprehension ...")
newlist_2 = [[w,w.upper(),len(w)] for w in words]
pprint.pprint(newlist_2, depth=2)
