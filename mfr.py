from functools import reduce
# Let's define some data
data = [
      ['Tokyo', 35676000.0, 'Capital'],
      ['New York', 19354922.0, 'Major'],
      ['Mexico City', 19028000.0, 'Capital'],
      ['Mumbai', 18978000.0, 'Major'],
      ['Sao Paulo', 18845000.0, 'Major'],
      ['Delhi', 15926000.0, 'Capital'],
      ['Shanghai', 14987000.0, 'Major'],
      ['Kolkata', 14787000.0, 'Major'],
      ['Los Angeles', 12815475.0, 'Major'],
      ['Dhaka', 12797394.0, 'Capital'],
      ['Buenos Aires', 12795000.0, 'Capital'],
      ['Karachi', 12130000.0, 'Major'],
      ['Cairo', 11893000.0, 'Capital'],
      ['Rio de Janeiro', 11748000.0, 'Major'],
      ['Osaka', 11294000.0, 'Major'],
      ['Beijing', 11106000.0, 'Capital'],
      ['Manila', 11100000.0, 'Capital'],
      ['Moscow', 10452000.0, 'Capital'],
      ['Istanbul', 10061000.0, 'Major'],
      ['Paris', 9904000.0, 'Capital']
]
# Method1 (standard)
list1 = []
for cinfo in data:
  if (cinfo[2] == 'Capital' and cinfo[1] > 10000000):
    list1.append(cinfo[0])

print(list1)

# Method 2 (functional)
map_obj = list(filter(lambda x: x[2] == 'Capital' and x[1] > 10000000, data))
map_obj = list(map(lambda x: x[0], map_obj))
map_obj = reduce(lambda x,y: x + ", " + y, map_obj, 'Cities:')
print(map_obj)

# Method 3 (List comprehension) 
list2 = [cinfo[0] for cinfo in data if cinfo[2] == 'Capital' and cinfo[1] > 10000000]
print(list2)
