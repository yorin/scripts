import urllib2
import re
import json

req ='http://www.google.com/finance/converter?a=1&from=USD&to=PHP'
#req ='http://www.google.com/finance/converter?a=1&from=USD&to=PHP?format=json'
#req = 'http://www.voidspace.org.uk'
response = urllib2.urlopen(req)
#print response.read()
#the_page = response.read()
raw_data = response.read()
#raw_data = raw_data.replace('\xa0','')
#j = req.sanitize(raw_data)
#data = json.loads(j)
#print raw_data
print re.search("<div id=currency_converter_result>.*", raw_data).group()
