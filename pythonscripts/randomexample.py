# random

import random

print random.choice(['apple', 'pear', 'banana'])
print random.sample(xrange(100), 10)   # sampling without replacement
print random.random()    # random float
print random.randrange(6)    # random integer chosen from range(6)

import time
t = time.time()
int(str(t-int(t))[2:])%100
