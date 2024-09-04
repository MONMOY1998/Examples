def square(items):
  for i,x in enumerate(items):
    items[i] = x * x # Modify items in-place

a = [1, 2, 3, 4, 5]
print a
square(a) # Changes a to [1, 4, 9, 16, 25]
print a
