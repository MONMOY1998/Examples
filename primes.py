#!/usr/bin/env python3

# nested LC
noprimes = [j for i in range(2, 8) 
           for j in range(i*2, 50, i)]
print(noprimes)

primes = [x for x in range(2, 50)
         if x not in noprimes]
print(primes)
