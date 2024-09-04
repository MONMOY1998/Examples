# 
# r = list(map(func, seq))
#

# using named functions
def fahrenheit(T):
  return ((float(9)/5)*T + 32)

def celsius(T):
  return (float(5)/9)*(T-32)

#temp = (36.5, 37, 37.5,39) # in C
F = [fahrenheit(36. + 0.5*ii) for ii in range(20)]
print(F)

C = list(map(celsius, F))
print(C)

# using anonymous functions
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, Celsius))
print(Fahrenheit)

C = list(map(lambda x: (float(5)/9)*(x-32), Fahrenheit))
print(C)
