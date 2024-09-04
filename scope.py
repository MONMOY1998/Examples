print("----- step 1 ------")
# global
a = 0

# global (but unlike c++ !!!)
if a == 0:
    b = 1

print(a)    # valid for any language
print(b)    # a little special

print("----- step 2 ------")

# local
def test_scope(c):
    d = 3
    print(c)
    print(d)

# call the function
d = 10
test_scope(7)

# c and d are truly local -- not visible anymore
print(c)
