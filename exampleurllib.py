import urllib2

req = 'http://www.voidspace.org.uk'
response = urllib2.urlopen(req)
print response.read()
#the_page = response.read()
