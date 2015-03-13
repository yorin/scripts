#!/usr/bin/python
import math

vara = 10
varb = 20

print "hello world!"

sum = vara + varb
difference = varb - vara
product = vara * varb
quotient = varb / vara
power = vara ** varb
root = varb ** (1.0/vara)
modulo = varb % vara
squareroota = math.sqrt(vara)
squarerootb = math.sqrt(varb)
print "sum of var a + var b = %d" % sum
print "differece of var b - var a = %d" %difference
print "product of var a * var b =  %d" %product
print "quotient of var b / var a =  %d" %quotient
print "power of var a exponent var b =  %d" %power
print "root of radicand var b degree var a =  %s" %root
print "var b mod var a =  %s" %modulo
print "square root of var a: %s square root of var b: %s" %(squareroota,squarerootb)
