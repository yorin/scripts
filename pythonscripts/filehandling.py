#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r+")
#read the fifth 
str = fo.read(5);
print "Read String is : ", str

#open a file
fo2 = open("foo.txt", "r+")
#read all
str2 = fo2.read();
print "Read all String: ", str2

# Close opend file
fo.close()
